# Kapsam Analizi
**Fatih Yumuşak - 20253006032**

Python değişken kapsamı LEGB kuralıyla çalışıyor: Local, Enclosing, Global, Built-in sırasıyla aranıyor.

---

## Örnek 1

```python
renk = "mavi"

def boya():
    renk = "kırmızı"
    print(renk)

boya()
print(renk)
```

**Tahminim:** önce kırmızı, sonra mavi yazdırır diye düşündüm.

**Gerçek sonuç:**
```
kırmızı
mavi
```

**Neden:** `boya()` içindeki `renk = "kırmızı"` satırı yeni bir yerel değişken oluşturuyor. Global `renk` değişmiyor çünkü Python fonksiyon kapsamında yeni bir kopya oluşturdu.

---

## Örnek 2

```python
puan = 100

def goster():
    print(puan)

goster()
```

**Tahminim:** 100 yazar

**Gerçek sonuç:**
```
100
```

**Neden:** Fonksiyon içinde `puan`'a atama yapılmıyor, sadece okunuyor. LEGB sıralamasıyla global `puan` bulunuyor ve yazdırılıyor.

---

## Örnek 3 - UnboundLocalError

```python
puan = 100

def guncelle():
    print(puan)
    puan = 200
    print(puan)

guncelle()
```

**Tahminim:** İlk print 100 yazar, sonra 200'e günceller diye düşündüm.

**Gerçek sonuç:**
```
UnboundLocalError: local variable 'puan' referenced before assignment
```

**Neden:** Python derleme aşamasında `puan = 200` satırını görünce `puan`'ı bu fonksiyon içinde yerel değişken olarak işaretliyor. Bu karar fonksiyonun tamamına uygulanıyor. Dolayısıyla ilk satırdaki `print(puan)` çalışmaya çalıştığında yerel `puan` henüz atanmamış, hata veriyor. Bunu anlamak biraz zaman aldı ama Python önce tüm fonksiyonu analiz edip hangi değişkenlerin yerel olduğuna karar veriyor.

Çözüm olarak değeri parametre olarak almak daha temiz:

```python
def guncelle(p):
    print(p)
    p = 200
    print(p)
```
