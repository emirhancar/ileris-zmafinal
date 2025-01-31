import requests
import csv
import os
from scapy.all import ARP, Ether, srp
import pandas as pd
from tabulate import tabulate

OUI_CSV_URL = "https://standards-oui.ieee.org/oui/oui.csv"
OUI_LOCAL_FILE = "oui.csv"

def update_mac_database():
    try:
        response = requests.get(OUI_CSV_URL)
        if response.status_code == 200:
            with open(OUI_LOCAL_FILE, "wb") as file:
                file.write(response.content)
            print("MAC veritabanı güncellendi.")
        else:
            print("Veritabanı güncellenemedi! (Status code: {})".format(response.status_code))
    except Exception as e:
        print(f"Veritabanı güncellenirken hata oluştu: {e}")

def get_vendor(mac_address):
    mac_prefix = mac_address.upper().replace(":", "")[:6] 
    
    if not os.path.exists(OUI_LOCAL_FILE):
        print("Veritabanı bulunamadı. Güncelleniyor...")
        update_mac_database()
    
    try:
        with open(OUI_LOCAL_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                if row[1].replace("-", "").upper() == mac_prefix:
                    return row[2]  
    except FileNotFoundError:
        print("MAC veritabanı bulunamadı. Lütfen tekrar deneyin.")
        return "Veritabanı hatası"
    except Exception as e:
        print(f"Veritabanı okunurken hata oluştu: {e}")
    
    return "Bilinmeyen Üretici" 

def is_fake_mac(mac_address):
    """MAC adresinin sahte (rastgele üretilmiş) olup olmadığını kontrol eder."""
    first_byte = int(mac_address[:2], 16)
    return (first_byte & 2) != 0  


def categorize_device(vendor):
    """Cihaz üreticisini kategorize eder."""
    categories = {
        "Apple": "Mobil Cihaz / Bilgisayar",
        "Cisco": "Ağ Cihazı",
        "Huawei": "Ağ / Mobil Cihaz",
        "Samsung": "Mobil Cihaz",
        "Intel": "Bilgisayar / Donanım",
        "TP-Link": "Ağ Cihazı",
        "Xiaomi": "IoT / Mobil Cihaz",
    }
    for key, category in categories.items():
        if key.lower() in vendor.lower():
            return category
    return "Bilinmeyen Kategori"

def scan_network(ip_range="192.168.1.1/24"):
    """Ağdaki cihazları tarar ve her bir cihazın bilgilerini döner."""
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  
    packet = ether / arp
    try:
        result = srp(packet, timeout=3, verbose=False)[0]
    except Exception as e:
        print(f"Ağ taraması sırasında hata oluştu: {e}")
        return []

    devices = []
    for sent, received in result:
        mac_address = received.hwsrc
        vendor = get_vendor(mac_address)
        category = categorize_device(vendor)
        is_fake = is_fake_mac(mac_address)
        devices.append({
            "IP": received.psrc,
            "MAC": mac_address,
            "Vendor": vendor,
            "Kategori": category,
            "Sahte MAC": "Evet" if is_fake else "Hayır"
        })
    
    return devices

if __name__ == "__main__":
    print("Ağ taraması başlatılıyor...")
    scanned_devices = scan_network()
    
    if scanned_devices:
        df = pd.DataFrame(scanned_devices)
        print(tabulate(df, headers="keys", tablefmt="grid"))
    else:
        print("Hiçbir cihaz bulunamadı!")
