from  pykeyboard import *
import time
from PIL import Image
from PIL import ImageGrab
import numpy as np
'''
def hash_img(img):#计算图片的特征序列
    a=[]#存储图片的像素
    hash_img=''#特征序列
    width,height=10,10#图片缩放大小
    img=img.resize((width,height))#图片缩放为width×height
    for y in range(img.height):
        b=[]
        for x in range(img.width):
            pos=x,y
            color_array = img.getpixel(pos)#获得像素
            color=sum(color_array)/3#灰度化
            b.append(int(color))
        a.append(b)
    for y in range(img.height):
        avg=sum(a[y])/len(a[y])#计算每一行的像素平均值
        for x in range(img.width):
            if a[y][x]>=avg:#生成特征序  列,如果此点像素大于平均值则为1,反之为0
                hash_img+='1'
            else:
                hash_img+='0'
                
    return hash_img
'''    
def similar(img):#求相似度
    im=np.array(img.convert("L"))
    ans=0
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if(im[i][j]<=130):
                ans=ans+1
    return ans
    
def similar2(img):#求相似度
    im=np.array(img.convert("L"))
    ans=0
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if(im[i][j]>=180):
                ans=ans+1
    return ans

    
#box=(350,586,451,687)

box2=(0,900,68,994)
k=PyKeyboard()
time.sleep(2)
k.tap_key(" ")
time.sleep(2)
t1=0.1
t2=0.01
t=0;
#k.press_key(k.down_key)
while 1:
    box=(486+t,618,634+t,688)
    box3=(381+3*t,543,491+3*t,594)
    
    img1=ImageGrab.grab(box)
    img3=ImageGrab.grab(box3)
    img2=ImageGrab.grab(box2)
    #img1.save("44.png")
    #img2=Image.open("5.png")
    #img3=Image.open("1.png")
    #img4=Image.open("6.png")
    #print('%.1f%%' % (similar(img1,img2) * 100))
    #time.sleep(0.1)
    
    
    
    im2=similar(img2)
    #print(im)
    
    if im2<=10:
        im3=similar(img3)
        im=similar(img1)
        if im3<2:   
            if im>=2 :
                #k.release_key(k.down_key)
               # time.sleep(0.1)
                k.press_key(k.up_key)
                time.sleep(0.1)
                k.release_key(k.up_key)
                time.sleep(t2)
                t1=t1*0.9996
                t2=t2*0.998
                t=t+0.8
                #k.press_key(k.down_key)
        else:
            k.press_key(k.up_key)
            time.sleep(0.1)
            k.release_key(k.up_key)
            time.sleep(t2)
            t2=t2*0.998
            t=t+0.8
    else:
        im3=similar2(img3)
        im=similar2(img1)
        if im3>=2:
            k.press_key(k.up_key)
            time.sleep(0.1)
            k.release_key(k.up_key)
            time.sleep(t2)
            t2=t2*0.998
            t=t+0.8
        else:
             if im>=2 :
               # k.release_key(k.down_key)
               # time.sleep(0.1)
                k.press_key(k.up_key)
                time.sleep(0.1)
                k.release_key(k.up_key)
                time.sleep(t2)
                t1=t1*0.9996
                t2=t2*0.998
                t=t+0.8
               # k.press_key(k.down_key)
    
       


   


