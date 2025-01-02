import turtle
import math

# MEHMET DÖNMEZ
# https://github.com/mehmetdonmezz



# Pencereyi oluştur
window = turtle.Screen()
window.bgcolor("black")

# Kalem ayarları
pen = turtle.Turtle()
pen.speed(0)  # En hızlı çizim hızı
pen.color("blue")

# Kalp şekli fonksiyonu
def heart(t, size=1):
    x = 16 * math.sin(t) ** 3 * size
    y = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * size
    return x, y

# Kalp çizen fonksiyon
def draw_heart(size=1, offset=(0, 0)):
    pen.penup()
    pen.goto(offset)
    pen.pendown()
    
    for t in range(0, 360, 15):  # Hız artırmak için adımı 1'e indirdim
        x, y = heart(math.radians(t), size)  # t'yi derece yerine radian olarak hesapla
        pen.goto(x + offset[0], y + offset[1])

# 10 kalp çizme döngüsü
i = 5000
for i in range(20):
    pen.speed(i + 100000)  # Her bir kalp çiziminde hız 1 artırılacak
    draw_heart(size=1 + 0.9 * i, offset=(0, 0))  # Her kalp bir öncekinden büyük olacak

# Animasyon bitmeden pencereyi kapatmamızı sağlar
turtle.done()
