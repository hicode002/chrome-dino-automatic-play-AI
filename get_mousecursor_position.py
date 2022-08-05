import pyautogui as pg    
try:
    while True:
        x,y=pg.position()               
        print(str(x)+" "+str(y)) #输出鼠标的x,y
except KeyboardInterrupt:
    print("\n")
