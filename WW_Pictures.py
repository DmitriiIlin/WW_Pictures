from PIL import Image, ImageDraw, ImageColor, ImageFont
import os.path
import random

def rect_painter(file_name):
    #Рисуем квадрат в центре изображения 
    image=Image.open(file_name)
    draw=ImageDraw.Draw(image)
    sz=image.size
    #print(sz)
    rect_size = 100
    draw.rectangle([sz[0]/2-rect_size,sz[1]/2-rect_size,sz[0]/2+rect_size,sz[1]/2+rect_size],fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    draw.text((sz[0]/2-rect_size/4,sz[1]/2-rect_size/4),"Hello \nworld",font = ImageFont.truetype("arial.ttf", 20), fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    image.save("test.jpg","JPEG")
    del draw
    

def change_extention (file_name_for_painting, input_ext = None, output_ext = None):
    #Функция ищет в текущем каталоге все файлы с расширением input_ext, в случае нахождения меняет расширения этих файлов на output_ext
    current_working_directory = os.getcwd()
    files_and_directories = os.listdir(current_working_directory)
    for files in files_and_directories:
        if files.endswith(input_ext):
            base_name = os.path.splitext(files)[0]
            ext_name = os.path.splitext(files)[1]
            os.rename(files,str(base_name)+"."+str(output_ext))
    rect_painter(file_name_for_painting)


