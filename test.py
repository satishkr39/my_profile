import PIL
import os
from PIL import Image

f = r'C:\Users\satissingh\PycharmProjects\MyProfile\my_profile\static'
for file in os.listdir(f):
    print(file)
    if file.endswith('yles'):
        continue
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((600,600))
    img.save(f_img)