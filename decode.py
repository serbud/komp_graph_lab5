from PIL import Image, ImageDraw
import sys
import json
from math import gcd

imageroute = sys.argv[1]
jsonroute = sys.argv[2]
handle = open(jsonroute, "r")

s = handle.read()
s = json.loads(s)


res = []
k1 = -1

for k in s:
    res.append([])
    k1 += 1
    for pair in k:
        for j in range(pair[1]):
            res[k1].append(pair[0])



image = Image.new("L", (len(res),len(res[0])), 0)  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
height = image.size[1]  # Определяем ширину.
width = image.size[0]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.


for row in range(len(res)):
    for col in range(len(res[0])):
        grey = res[col][row]
        draw.point((col, row), grey)

image.save(imageroute, "BMP")
del draw

print("декодирование завершено")
