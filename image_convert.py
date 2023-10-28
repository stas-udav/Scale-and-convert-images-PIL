#!/usr/bin/env python3
from PIL import Image
import os
folder_path = "D:\\movavi video"

# Reciving files from the original folder
file_list = os.listdir(folder_path)

#create folder for new files
folder = "D:\\movavi video\\opt\\icons\\"

if not os.path.exists(folder):
    os.makedirs(folder)
# iteration over files
for filename in file_list:
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        image_path = os.path.join(folder_path, filename)
        im = Image.open(image_path)
        print(im.format, im.size)
        destination_path = os.path.join(folder, filename) #создаем абсолютный путь для сохранения файлов
        rotated  = im.rotate(90)
        out = rotated.resize((128, 128)) # изменяем размер повернутых файлов
        out.save(destination_path, "JPEG")
        im.close()
        rotated.close()
        out.close()
        
