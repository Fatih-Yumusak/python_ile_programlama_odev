# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Saniyeyi gün, saat, dakika, saniyeye ayırır.

toplam = int(input("Saniye: "))

gun = toplam // 86400          # 1 gün = 86400 saniye
kalan = toplam % 86400
saat = kalan // 3600
kalan = kalan % 3600
dakika = kalan // 60
saniye = kalan % 60

print(toplam, "saniye =", gun, "gün", saat, "saat", dakika, "dakika", saniye, "saniye")
