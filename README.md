

# MAC Vendor Analiz Sistemi

Bu proje, ağdaki cihazların **MAC adreslerini analiz ederek** üretici bilgilerini çıkaran, cihaz kategorilerini belirleyen ve sahte MAC adreslerini tespit eden bir sistemdir.  

## 🚀 Özellikler  
✅ **Güncel MAC Vendor Veritabanı Yönetimi** – IEEE OUI veritabanını kullanarak üreticileri belirler.  
✅ **Cihaz Kategorizasyonu** – MAC adresine göre cihazları IoT, ağ ekipmanı, mobil cihaz gibi kategorilere ayırır.  
✅ **Sahte MAC Adresi Tespiti** – Rastgele oluşturulmuş MAC adreslerini tespit eder.  
✅ **Vendor Bazlı Güvenlik Değerlendirmesi** – Belirli üreticilere ait cihazların güvenlik risklerini analiz eder.  

---

## 📌 Kurulum  

### 1️⃣ Gerekli Kütüphaneleri Yükleyin  
Python'un yüklü olduğundan emin olun. Daha sonra şu komutu terminalde çalıştırın:  

```bash
pip install requests scapy pandas tabulate

Eğer requests yüklenmezse, alternatif olarak şunu deneyin:

python -m pip install requests

2️⃣ Projeyi Klonlayın

GitHub üzerindeki projeyi bilgisayarınıza indirin:

git clone https://github.com/kullanici_adi/mac-vendor-analiz.git
cd mac-vendor-analiz

3️⃣ Python Sanal Ortamı (Önerilir)

Bağımlılıkları izole etmek için bir sanal ortam oluşturun:

python -m venv venv
source venv/bin/activate  # macOS/Linux için
venv\Scripts\activate  # Windows için

4️⃣ Python Kodunu Çalıştırın

Ağınızdaki cihazları taramak için şu komutu çalıştırın:

python mac_vendor_analyzer.py

Çalıştırdığınızda, şu şekilde bir çıktı alabilirsiniz:

Ağ taraması başlatılıyor...
+---------------+-------------------+------------------+-----------------------+------------+
| IP            | MAC               | Vendor           | Kategori              | Sahte MAC  |
+---------------+-------------------+------------------+-----------------------+------------+
| 192.168.1.2   | 00:1A:2B:3C:4D:5E | Cisco Systems    | Ağ Cihazı             | Hayır      |
| 192.168.1.3   | 02:AB:CD:EF:12:34 | Bilinmeyen Üretici | Bilinmeyen Kategori | Evet       |
| 192.168.1.4   | 58:9C:FC:12:34:56 | Apple Inc.       | Mobil Cihaz / Bilgisayar | Hayır  |
+---------------+-------------------+------------------+-----------------------+------------+

⚙️ Teknik Detaylar
	•	Scapy kütüphanesi kullanılarak ağdaki cihazlar tespit edilir.
	•	IEEE OUI Veritabanı üzerinden MAC adresinin üreticisi belirlenir.
	•	MAC Adresi Kategorizasyonu ile cihaz türü tahmin edilir.
	•	Sahte MAC Tespiti için MAC adresinin ilk baytı incelenir.

📄 Lisans

Bu proje MIT Lisansı ile yayınlanmıştır. İstediğiniz gibi kullanabilir, geliştirebilir veya paylaşabilirsiniz.

🤝 Katkıda Bulunma

Katkıda bulunmak isterseniz:
	1.	Fork yapın 🍴
	2.	Yeni bir özellik geliştirin 🚀
	3.	PR (Pull Request) açın 📥

Her türlü katkıya açığız!

📞 İletişim

Geliştirici: emirhancar

---


https://github.com/user-attachments/assets/f1c4b9d3-dfb0-4e1c-90f4-99b907a8793e


