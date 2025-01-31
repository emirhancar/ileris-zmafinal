
Eklenenler:
Ağ tarama aracına yeni cihaz kategorileri ekledi.
MAC adresi üzerinden sahte cihaz tespiti eklendi.
IEEE OUI veritabanını internetten güncelleyebilecek yeni fonksiyon eklendi.
Ağ taraması sonucu cihazların bilgilerini daha okunabilir bir formatta göstermek için tabulate kütüphanesi eklendi.
Düzeltmeler:
OUI veritabanı bulunamadığında kullanıcıya güncelleme yapılacağına dair bilgi verildi.
Ağ tarama sırasında oluşabilecek FileNotFoundError ve diğer hata durumlarına karşı daha sağlam hata yönetimi eklendi.
[1.0.0] - 2025-01-31
Eklenenler:
IEEE OUI veritabanından cihaz üretici bilgilerini almak için fonksiyon eklendi.
Ağ tarama fonksiyonu (scan_network) yazıldı, bu fonksiyon, ağdaki cihazları tespit edip MAC adresi, IP adresi, üretici adı, cihaz kategorisi gibi bilgileri döner.
Cihazların kategorilerine göre sınıflandırılması sağlandı. Örneğin, "Apple" cihazları "Mobil Cihaz / Bilgisayar" olarak sınıflandırıldı.
Sahte MAC adreslerini tespit etme fonksiyonu eklendi.
Düzeltmeler:
OUI_LOCAL_FILE'in mevcut olup olmadığını kontrol etmek için fonksiyonlar iyileştirildi. Eğer dosya yoksa otomatik olarak güncellenmesi sağlandı.
[0.1.0] - 2025-01-15
Eklenenler:
İlk sürüm.
MAC adresi üzerinden cihaz üreticisi bilgilerini almak için temel fonksiyonlar yazıldı.
Ağ tarama ile ağdaki cihazların MAC adresleri tespit edilmeye başlandı.
