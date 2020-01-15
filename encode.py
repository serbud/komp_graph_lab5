from PIL import Image, ImageDraw
import sys
import json

imageroute = sys.argv[1]

image = Image.open(imageroute)  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
height = image.size[1]  # Определяем ширину.
width = image.size[0]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.



res = []

for i in range(height):
    res.append([])
    lst = pix[i, 0]
    count = 1
    for j in range(1,width,1):
        prs = pix[i, j]  # перевод в оттенки серого
        if prs == lst:
            count += 1
        else:
            res[i].append((lst, count))
            count = 1
            lst = prs
    res[i].append(tuple((lst, count)))


name = imageroute.split(".")[0]
handle = open(f"{name}.json", "w")
handle.write(json.dumps(res))
handle.close()
