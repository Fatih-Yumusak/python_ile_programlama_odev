# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Turtle ile kare + üçgenden oluşan ev çizer ve adı yazar.

import turtle

# Kare (gövde): sol alt köşeden başlar
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# Kalemi kaldırmadan sol üst köşeye çık
turtle.left(90)
turtle.forward(100)
turtle.right(90)

# Eşkenar üçgen (çatı): her dönüş 120 derece
for _ in range(3):
    turtle.forward(100)
    turtle.left(120)

# Evin yanına ad yaz
turtle.penup()
turtle.goto(130, 0)
turtle.write("Fatih", font=("Arial", 16, "normal"))
turtle.hideturtle()
turtle.done()
