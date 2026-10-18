# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: 0-999 arası sayının rakamlarını toplar.

sayi = int(input("Sayı (0-999): "))

birler = sayi % 10             # son rakam
kalan = sayi // 10
onlar = kalan % 10
yuzler = kalan // 10

print("Rakamlar toplamı:", birler + onlar + yuzler)
