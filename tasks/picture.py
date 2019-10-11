from graph import *
import math

def Amazing(k, d):
    penColor("black")
    brushColor("orange")
    circle(int(k*200+d), int(k*430), int(k*160))
    (i1, i2, k1, k2, l1, l2, m1, m2, o1, o2) = (60, 300, 100, 280, 130, 320, 110, 350, 65, 330)
    polygon([(int(k*i1+d), int(k*i2)), (int(k*k1+d),int(k*k2)), (int(k*l1+d), int(k*l2)), (int(k*m1+d),int(k*m2)), (int(k*o1+d), int(k*o2))])
    polygon([(int(k*(400-i1)+d), int(k*(i2))), (int(k*(400-k1)+d),int(k*(k2))), (int(k*(400-l1)+d), int(k*(l2))), (int(k*(400-m1)+d),int(k*(m2))), (int(k*(400-o1)+d), int(k*(o2)))])
    brushColor((245, 175, 175))
    polygon([(int(k*40+d), int(k*40)), (int(k*60+d),int(k*40)), (int(k*(i1+3*k1)/4+d), int(k*(i2+3*k2)/4)), (int(k*(3*i1+k1)/4+d),int(k*(3*i2+k2)/4))])
    polygon([(int(k*360+d), int(k*40)), (int(k*340+d),int(k*40)), (int(k*(400-(i1+3*k1)/4)+d), int(k*(i2+3*k2)/4)), (int(k*(400-(3*i1+k1)/4+d)),int(k*(3*i2+k2)/4))])
    penColor("white")
    circle(int(k*50+d), int(k*40), int(k*20))
    circle(int(k*350+d), int(k*40), int(k*20))
    penColor((245, 175, 175))
    circle(int(k*200+d), int(k*200), int(k*100))
    penColor("black")
    brushColor("brown")
    polygon([(int(k*206+d),int(k*200)), (int(k*200+d), int(k*210)), (int(k*194+d),int(k*200))])
    brushColor("red")
    polygon([(int(k*160+d),int(k*220)), (int(k*200+d), int(k*250)), (int(k*240+d),int(k*220))])
    brushColor("lightblue")
    circle(int(k*230+d), int(k*180), int(k*20))
    circle(int(k*170+d), int(k*180), int(k*20))
    brushColor("black")
    circle(int(k*230+d), int(k*180), int(k*5))
    circle(int(k*170+d), int(k*180), int(k*5))
    brushColor("violet")
    s = 18
    for i in range(10):
        polygon([(int(k*(200+math.cos(math.pi*(135-10*i)/180)*(100+s))+d), int(k*(200-math.sin(math.pi*(135-10*i)/180)*(100+s)))), (int(k*(200+math.cos(math.pi*(128-10*i)/180)*100)+d), int(k*(200-math.sin(math.pi*(128-10*i)/180)*100))), (int(k*(200+math.cos(math.pi*(142-10*i)/180)*100)+d), int(k*(200-math.sin(math.pi*(142-10*i)/180)*100)))])
    
k = 0.5
windowSize(int(400*k), int(400*k))
brushColor("black")
polygon([(0, 0), (int(k*400), 0), (int(k*400), int(k*400)), (0, int(k*400))])
Amazing(k, 0)
brushColor("lime")
polygon([(0,0), (400*k, 0), (400*k, 40*k), (0, 40*k)])
label("P Y T H O N  i s  A M A Z I N G", 30*k, 0, bg="lime")
run()
