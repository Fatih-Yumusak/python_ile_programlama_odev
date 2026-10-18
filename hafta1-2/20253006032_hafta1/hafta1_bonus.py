# Ad Soyad: Fatih Yumuşak
# Öğrenci No: 20253006032
# Tarih: 04/10/2026
# Açıklama: Turtle ile olimpiyat halkalarını çizer.

import turtle

turtle.width(4)
halkalar = [("blue", -110, 0), ("black", 0, 0), ("red", 110, 0),
            ("yellow", -55, -50), ("green", 55, -50)]

for renk, x, y in halkalar:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(renk)
    turtle.circle(50)

turtle.hideturtle()
turtle.done()
