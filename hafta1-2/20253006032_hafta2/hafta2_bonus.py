# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Gün, saat, dakika, saniyeden toplam saniyeyi bulur.

gun = int(input("Gün: "))
saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))

print("Toplam saniye:", gun * 86400 + saat * 3600 + dakika * 60 + saniye)
