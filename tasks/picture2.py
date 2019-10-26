from graph import *

# (230,230,230) - grey color
# (0,255,255) - sky color
# (170,255,255) - sun color
# (230,230,230) - bear color

def elipsfill(x,y, x0, y0, a, b)  :
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1):
        return True
    else :
        return False
   
def elipsboard (x,y, x0, y0, a, b):
    e = 0.032
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1+e
         and
         (x-x0)**2/(a**2) + (y-y0)**2/(b**2) >= 1-e) :
        return True
    else :
        return False
   
def contur_elips(x0,y0, a, b):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsboard (x,y, x0, y0, a, b):
                 point (x,y,"black")          
def elips(x0, y0, a, b, color):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if elipsfill(x,y, x0, y0, a, b):
                point(x,y,color)
    contur_elips(x0,y0, a, b)

def Fish(x0, y0, s, f, h): #x = 380, y = 565
    elips(x0,y0,int(s*40),int(s*15),(180,180,180)) #body

    penColor(100,100,255) #eye
    brushColor(100,100,255)
    circle(x0+f*int(s*25),y0-h*int(s*5), int(s*6))
    penColor("black")
    brushColor("black")
    circle(x0+f*int(s*25), y0-h*int(s*5), int(s*3))

    penColor("black")
    brushColor(180,180,180)
    polygon([(x0-f*int(s*40),y0), (x0-f*int(s*80),y0-h*int(s*10)), (x0-f*int(s*85),y0+h*int(s*15))]) #tail

    penColor(255,100,100)
    brushColor(255,200,200)

    polygon([(x0+f*int(s*15), y0-h*int(s*15)), (x0+f*int(s*10), y0-h*int(s*30)), (x0-f*int(s*30),y0-h*int(s*27)), (x0-f*int(s*5), y0-h*int(s*15))]) #fins
    polygon([(x0-f*int(s*5), y0+h*int(s*15)), (x0-f*int(s*5),y0+h*int(s*25)), (x0-f*int(s*25),y0+h*int(s*25)), (x0-f*int(s*15),y0+h*int(s*15))])
    polygon([(x0+f*int(s*5),y0+h*int(s*15)), (x0+f*int(s*15), y0+h*int(s*15)), (x0+f*int(s*35),y0+h*int(s*25)), (x0+f*int(s*5),y0+h*int(s*25)), ])
    
def Bear(x0, y0, s, f): #x = 100, y = 410
    elips(x0+f*int(s*30),y0-int(s*165),int(s*50),int(s*30), (230,230,230)) #head
    elips(x0,y0,int(s*75),int(s*150), (230,230,230)) #body
    elips(x0+f*int(s*75),y0+int(s*115),int(s*60),int(s*40), (230,230,230)) #leg
    elips(x0+f*int(s*140),y0+int(s*140),int(s*30),int(s*12), (230,230,230)) #foot
    penColor("black") #nose
    brushColor("black")
    circle(x0+f*int(s*80),y0-int(s*170),int(s*4))
    circle(x0+f*int(s*25),y0-int(s*173),int(s*4)) #eye
    line(x0+f*int(s*35),y0-int(s*155),x0+f*int(s*78),y0-int(s*155)) #mouth
    brushColor(230,230,230) #ear
    circle(x0-f*int(s*5),y0-int(s*185),int(s*7))
    elips(x0+f*int(s*260),y0+int(s*80),int(s*80),int(s*30), (100,100,100)) #loonka
    elips(x0+f*int(s*260),y0+int(s*90),int(s*65),int(s*20), (40,100,90)) #water
    penColor("black")
    line(x0+f*int(s*260),y0-int(s*210),x0+f*int(s*260),y0+int(s*90))
    penSize(3)
    line(x0+f*int(s*260),y0-int(s*210),x0+f*int(s*25),y0)
    penSize(1)
    elips(x0+f*int(s*75),y0-int(s*50),int(s*40),int(s*15),  (230,230,230)) #arm
    Fish(x0+f*int(s*280), y0+int(s*145), 0.8*s, f, 1)
    Fish(x0+f*int(s*270), y0+int(s*155), 0.7*s, -f, 1)
    Fish(x0+f*int(s*230), y0+int(s*175), 0.7*s, f, 1)
    Fish(x0+f*int(s*310), y0+int(s*185), 0.7*s, -f, 1)
    Fish(x0+f*int(s*210), y0+int(s*35), 0.3*s, f, -1)
    Fish(x0+f*int(s*250), y0+int(s*25), 0.3*s, -f, 1)
    Fish(x0+f*int(s*285), y0+int(s*35), 0.3*s, -f, -1)

    
windowSize(500,600)

brushColor(0,255,255)
rectangle(0, 0, 500, 350 )

brushColor(230,230,230)
rectangle(0, 350, 500, 800 )

penColor(170,255,255) #outside circle
brushColor(170,255,255)
circle(310,110,110)

penColor(0,255,255) #inside circle
brushColor(0,255,255)
circle(310,110,90)

penColor(170,255,255) #lights
brushColor(170,255,255)
rectangle(300,0,320,220)
rectangle(200,120,420,100)

penColor("white") #circles
brushColor("white")
circle(310,110,15)
circle(210,110,10)
circle(310, 10,10)
circle(410,110,10)
circle(310,210,10)
#-----------------
Bear(33, 500, 0.3, 1)
Bear(250, 400, 0.3, -1)
Bear(460, 350, 0.2, -1)
Bear(490, 560, 0.5, -1)
#-------------------------------------


run()
