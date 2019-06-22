# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:55:39 2019

@author: venkatesh avula
"""


#Constants---------------------------------------------------
Fonts = ["Times", "Arial", "Verdana","comic", "Tahoma", "Calibri","Lsans","MTCORSVA","CALIFR","Rock","ShowG"] #file names : *.ttf fonts
#Fonts = ['Times', "Arial", "Verdana","comic", "Tahoma", "Calibri","Lsans","MTCORSVA","CALIFR","Rock","ShowG"] #file names : *.ttf fonts
FontsFolder= 'c:/Windows/Fonts/'
ImgSize=32
StddevMax=200#max nose level
FontSize=25 #font size in the image

import math
import random
from PIL import ImageFont, ImageDraw, Image, ImageFilter
import numpy as np


def add_noise(x, mean, stddev):
    return min(max(0, x+random.normalvariate(mean,stddev)), 255)


def add_noise_one_pixel(img, x, y, mean, stddev):
     r, g, b = img.getpixel((x,y))
     img.putpixel((x,y), (int(add_noise(r, mean, stddev)), int(add_noise(g, mean, stddev)), int(add_noise(b, mean, stddev))))
     return
 

def add_noise_img(img, mean, stddev): 
    X,Y= img.size
    for x in range(X):
        for y in range(Y):
            add_noise_one_pixel(img, x, y, mean, stddev)
    return img      



def MakeDataset2(N):
    font_types=len(Fonts)
    D=ImgSize*ImgSize
    nIndivualFont=N/font_types 
    x=np.zeros((N,D))
    y=np.zeros((N,1))
    
    for i in range(N):
        fonttype=math.floor(i/nIndivualFont)
        data=ImgData(fonttype)
        x[i,:]=data[:,0]
        y[i]=fonttype
    return x,y    
    

def MakeDataset(N):
    font_types=len(Fonts)
    D=ImgSize*ImgSize
    nIndivualFont=N/font_types 
    x=np.zeros((N,D))
    y=np.zeros((N,1),dtype='S4')
    
    for i in range(N):
        fonttype=math.floor(i/nIndivualFont)
        data=ImgData(fonttype)
        x[i,:]=data[:,0]
        y[i]=Fonts[fonttype].encode().decode('utf8')
    return x,y    
       
    

def ImgData(fonttype):
    
    D=ImgSize*ImgSize
    vecImage=np.zeros((D,1))
    mean = 0.0
    stddev = random.uniform(0, StddevMax)    # standard deviation
    
    
    img = Image.new('RGB', (ImgSize, ImgSize), color = (255,255,255))

    fontname=Fonts[fonttype]+'.ttf'
        
    fnt = ImageFont.truetype(FontsFolder+fontname, FontSize)
    d = ImageDraw.Draw(img)
    d.text((2,2), "H", font=fnt, fill=(0,0,0)) #test starts at 2 pixels
    #img.save('Times_text_font25T.png')
    
    #noisy font
    img=add_noise_img(img,mean,stddev)
    imgData=list(img.getdata())
    for i in range(D):
        (r,g,b)=imgData[i]
        vecImage[i]=r
        
    return vecImage     