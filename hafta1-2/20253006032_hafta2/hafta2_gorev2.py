# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Silindirin taban alanını ve hacmini hesaplar.

PI = 3.14159

yaricap = float(input("Yarıçap: "))
yukseklik = float(input("Yükseklik: "))

taban_alani = PI * yaricap ** 2
hacim = taban_alani * yukseklik

print("Taban alanı:", round(taban_alani, 7))
print("Hacim:", round(hacim, 7))
