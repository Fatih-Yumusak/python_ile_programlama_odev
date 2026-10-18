# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Aylık bileşik faizle gelecekteki değeri hesaplar.

anapara = float(input("Anapara (TL): "))
faiz = float(input("Yıllık faiz (%): "))
sure = float(input("Süre (yıl): "))

gelecek_deger = anapara * (1 + faiz / (12 * 100)) ** (12 * sure)

print("Gelecekteki değer:", round(gelecek_deger, 2), "TL")
