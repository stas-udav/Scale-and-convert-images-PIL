#!/usr/bin/env python3
from PIL import Image
import os
folder_path = "D:\\movavi video"

# Получение списка файлов в указанной папке
file_list = os.listdir(folder_path)

# Итерация по файлам
for filename in file_list:
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        image_path = os.path.join(folder_path, filename)
        im = Image.open(image_path)
        print(im.format, im.size)
        destination_path = os.path.join("D:\\movavi video\\test", filename)
        rotated  = im.rotate(45)
        out = rotated.resize((128, 128))
        out.save(destination_path)
        im.close()
        rotated.close()
        out.close()
        
