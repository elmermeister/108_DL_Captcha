from PIL import Image ,ImageDraw, ImageFont, ImageFilter,ImageColor
import random
import os
import pandas as pd
import numpy as np

'''image parameter'''

size=(200,60)
mode="RGB"
bg_color=(255,255,255,0)
length=6
(width,height)=size

'''Set Font'''
fontpath='Fonts'
font_type=[]
for fonts in os.listdir(fontpath):
    if os.path.isfile(os.path.join(fontpath,fonts)):
        font_type.append(fonts)

print(font_type)

'''Set Code'''

#letter="abcdefghijklmnopqrstuvwxyz"
letter="abcdefghijklmnopqrstuvwxyz"
upper_letter=letter.upper()
number=''. join(map(str, range(0, 10)))
#init_chars = ''.join((letter, upper_letter, number))
init_chars = ''.join(( upper_letter, number))
print(init_chars)

def shift_code():
    code=random.sample(init_chars,length)
    strs= ''.join(code)

    bg_color=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
    font_color=(random.randint(0,100),random.randint(0,100),random.randint(0,100))
    im=Image.new("RGB",(200,60),bg_color)
    draw=ImageDraw.Draw(im)

    font=ImageFont.truetype(os.path.join(fontpath,font_type[0]),random.randint(20,30))
    for num, i in enumerate(code):
        x,y=(5+num*29,11+num*30)
#         print(x,y)
        draw.text((random.randint(x,y),random.randint(5,20)),str(i),font=font,fill=font_color)

    return im ,strs


def rotate_code():

    code=random.sample(init_chars,length)
    strs= ''.join(code)
    bg_color=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
    font_color=(random.randint(0,50),random.randint(0,50),random.randint(0,50))
    pic=Image.new("RGB",(200,60),bg_color)
    font=ImageFont.truetype(os.path.join(fontpath,font_type[0]),random.randint(20,25))
    for num ,char in enumerate (code):
        textpic=Image.new("RGBA",(30,30),bg_color)
        drawtext=ImageDraw.Draw(textpic)
        w,h=drawtext.textsize(char,font=font)
        drawtext.text(((30-w)/2,(30-h)/2),char,font=font,fill=font_color)
        textpic=textpic.rotate(random.randint(-45,45))
        textpic=textpic.resize((30,30))
        fff = Image.new('RGBA', (30,30), bg_color)
        out = Image.composite(textpic, fff, textpic)
        out.convert("RGB")
        x,y=(5+num*33,10+num*33)
        pic.paste(out,(random.randint(x,y),random.randint(5,20)))
    return pic,strs

def gradient_color():
    r,g,b = random.randint(150,255), random.randint(150,255), random.randint(150,255)
    img = Image.new("RGB", (200,60), (random.randint(150,255), random.randint(150,255), random.randint(150,255)))
    draw = ImageDraw.Draw(img)

#     r,g,b = random.randint(150,255), random.randint(150,255), random.randint(150,255)
    dr = (random.randint(100,300) - r)/150.
    dg = (random.randint(100,300) - g)/150.
    db = (random.randint(100,300) - b)/150.
#     print(r,g,b)
#     print(dr,dg,db)
    for i in range(60):
        r,g,b = r+dr, g+dg, b+db
        draw.line((0,i,200,i), fill=(int(r),int(g),int(b)))

    return img

def gradient_shift_code():
    def gradient_color():
        r,g,b = random.randint(150,255), random.randint(150,255), random.randint(150,255)
        img = Image.new("RGB", (200,60), (random.randint(150,255), random.randint(150,255), random.randint(150,255)))
        draw = ImageDraw.Draw(img)

    #     r,g,b = random.randint(150,255), random.randint(150,255), random.randint(150,255)
        dr = (random.randint(100,300) - r)/150.
        dg = (random.randint(100,300) - g)/150.
        db = (random.randint(100,300) - b)/150.
    #     print(r,g,b)
    #     print(dr,dg,db)
        for i in range(60):
            r,g,b = r+dr, g+dg, b+db
            draw.line((0,i,200,i), fill=(int(r),int(g),int(b)))

        return img
    code=random.sample(init_chars,length)
    strs= ''.join(code)

#     bg_color=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
    font_color=(random.randint(0,100),random.randint(0,100),random.randint(0,100))
    im= gradient_color()
    draw=ImageDraw.Draw(im)

    font=ImageFont.truetype(os.path.join(fontpath,font_type[0]),random.randint(20,30))
    for num, i in enumerate(code):
        x,y=(5+num*29,11+num*30)
#         print(x,y)
        draw.text((random.randint(x,y),random.randint(5,20)),str(i),font=font,fill=font_color)

    point_chance = 3
    chance = min(50, max(0, int(point_chance))) # 大小限制

    for w in range(width):
        for h in range(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w,h), fill=font_color)

    return im ,strs


def bg_shift_code():
    bgfold='resize'
    bglist=os.listdir(bgfold)[:25]
    bg=os.path.join(bgfold,bglist[random.randint(0,len(bglist)-1)])
    code=random.sample(init_chars,length)
    strs= ''.join(code)

#     bg_color=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
    font_color=(random.randint(50,200),random.randint(50,200),random.randint(100,200))
    im= Image.open(bg)
#     bg_color=max(im.getcolors(maxcolors=50000))[1]
#     font_color=changecolor(bg_color,CA)
#     im=Image.new("RGB",(200,60),bg_color)
    draw=ImageDraw.Draw(im)

    font=ImageFont.truetype(os.path.join(fontpath,font_type[random.randint(0,2)]),random.randint(25,30))
    for num, i in enumerate(code):
        x,y=(5+num*27,11+num*30)
#         print(x,y)
        draw.text((random.randint(x,y),random.randint(0,30)),str(i),font=font,fill=font_color)
    draw.line([(0,30), (200,30)], fill='white',width= 2)
    return im ,strs


def bg_rotate_noise_code():
    bgfold='resize'
    bglist=os.listdir(bgfold)
    bg=os.path.join(bgfold,bglist[random.randint(0,len(bglist)-1)])
    code=random.sample(init_chars,length)
    strs= ''.join(code)
#     bg_color=(random.randint(150,255),random.randint(150,255),random.randint(150,255))
#     font_color=(random.randint(30,50),random.randint(100,150),random.randint(150,200))
#     pic=Image.new("RGB",(200,60),bg_color)
    pic=Image.open(bg)
#     font=ImageFont.truetype(os.path.join(fontpath,font_type[2]),random.randint(20,25))
    for num ,char in enumerate (code):
        font=ImageFont.truetype(os.path.join(fontpath,font_type[random.randint(0,len(font_type)-1)]),random.randint(20,28))
        textpic=Image.new("RGBA",(30,30),(255,255,255,0))
        drawtext=ImageDraw.Draw(textpic)
        w,h=drawtext.textsize(char,font=font)
        font_color=(random.randint(0,150),random.randint(0,100),random.randint(0,255))
        drawtext.text(((30-w)/2,(30-h)/2),char,font=font,fill=font_color)
        textpic=textpic.rotate(random.randint(-45,45))
        textpic=textpic.resize((30,30))
#         fff = Image.new('RGBA', (30,30), bg_color)
#         out = Image.composite(textpic, fff, textpic)
#         out.convert("RGBA")
        x,y=(5+num*33,10+num*33)
        pic.paste(textpic,(random.randint(x,y),random.randint(0,30)),textpic)

    draw=ImageDraw.Draw(pic)
#     point_chance = 10
#     chance = min(100, max(0, int(point_chance))) # 大小限制

#     for w in range(width):
#         for h in range(height):
#             tmp = random.randint(0, 100)
#             if tmp > 100 - chance:
#                 draw.point((w, h), fill=font_color)

#     draw.line([(0,random.randint(0,20)), (200,random.randint(40,60))], fill=(0,0,0),width=2)
#     draw.line([(0,random.randint(40,60)), (200,random.randint(0,20))], fill=(0,0,0),width=2)
    line_num = random.randint(1,3) # 數量
#     print(line_num)
    linecolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for i in range(line_num):

        if(i==0):
            draw.line([(0,30), (200,30)], fill='white',width= 2)
        elif(i==1):
            linecolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            draw.line([(0,random.randint(0,20)), (200,random.randint(40,60))], fill=linecolor,width= 1)
        else:
            linecolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            draw.line([(0,random.randint(40,60)), (200,random.randint(0,20))], fill=linecolor,width= 1)

    return pic,strs
