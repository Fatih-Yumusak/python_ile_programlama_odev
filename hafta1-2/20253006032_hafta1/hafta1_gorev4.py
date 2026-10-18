# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Üç hata türünü gösterir ve düzeltir.

# A - Sözdizimi (syntax) hatası: tırnak kapatılmamış, Python kodu ayrıştıramaz.
# print("Merhaba Dünya)
print("Merhaba Dünya")

# B - Çalışma zamanı (runtime) hatası: sıfıra bölme (ZeroDivisionError).
# Kod sözdizimi olarak doğru ama çalışırken hata verir.
# print(10 / 0)
print(10 / 2)

# C - Mantık (logic) hatası: program çalışır ama yanlış sonuç verir.
# Önce bölme yapıldığı için 3 + 2.5 = 5.5 çıkar; toplamın parantez içinde olması gerekir.
# print(3 + 5 / 2)
print((3 + 5) / 2)
