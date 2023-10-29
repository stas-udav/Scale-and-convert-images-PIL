#!/usr/bin/env python3

import os
import PIL
from PIL import Image
import tifffile
import imageio

folder_path = "D:\\QA\\images"

# Reciving files from the original folder
file_list = os.listdir(folder_path)

#create folder for new files
folder = "D:\\movavi video\\opt\\icons\\"

if not os.path.exists(folder):
    os.makedirs(folder)
# iteration over files
for filename in file_list:
    #if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        image_path = os.path.join(folder_path, filename)
        im = Image.open(image_path)
        # Check the image mode and convert if necessary
        #if im.mode != 'RGB':
        im = im.convert('RGB')
        # if im.mode == 'LA' or im.mode == 'P':
        #     im = im.convert('RGB')
        # elif im.mode == 'P':
        #     im = im.convert('RGB')               
        #print(im.format, im.size)
        destination_path = os.path.join(folder, filename) #create path for saving new files
        rotated  = im.rotate(90)
        out = rotated.resize((128, 128)) # change size and rotation
        out.save(destination_path, format="JPEG")
        im.close()
        rotated.close()
        out.close()
         # Print format and size

#print(f"File: {filename}, Format: {im.format}, Size: {im.size}")
# List the saved files in the destination folder
saved_files = os.listdir(folder)
for saved_file in saved_files:
    saved_file_path = os.path.join(folder, saved_file)
    saved_im = Image.open(saved_file_path)
    print("Saved File:", saved_file, "Format:", saved_im.format, "Size:", saved_im.size)
        
