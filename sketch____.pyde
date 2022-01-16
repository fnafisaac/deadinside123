x = 500
y = 500
def setup():
    size(1000,1000)
    rectMode(CENTER)
def draw():
    global x, y
    background(0)
    if mousePressed:
        if mouseX > x-25 and mouseX < x+25 and mouseY  > y-25 and mouseY < y+25:
            mouseDragged()
    rect( x , y ,50,50)   
def mouseDragged():
    global x,y
    x = mouseX
    y = mouseY
    if x > 1000:
        x=999
            
