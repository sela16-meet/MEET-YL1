#PAINT
#Ye

brushtype = "circle"
brushsize = 1
brushcolor = "blue"
import turtle
5
turtle.ht()
turtle.speed("fastest")

def draw_square(x,y): #draws a square
    turtle.color(brushcolor)
    turtle.pu()
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pd()
    turtle.goto(x,y+10*brushsize)
    turtle.goto(x+10*brushsize,y+10*brushsize)
    turtle.goto(x+10*brushsize,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.pu()







def draw_circle(x,y): #draws a circle
    turtle.color(brushcolor)
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(10*brushsize)
    turtle.end_fill()
    turtle.pu()

def change_to_square():
    global brushtype
    brushtype = "square"

def change_to_circle():
    global brushtype
    brushtype = "circle"

def change_size_1():
    global brushsize
    brushsize = 1

def change_size_2():
    global brushsize
    brushsize = 2

def change_size_3():
    global brushsize
    brushsize = 3

def change_size_4():
    global brushsize
    brushsize = 4

def change_size_4():
    global brushsize
    brushsize = 4

def change_size_5():
    global brushsize
    brushsize = 5

def change_size_6():
    global brushsize
    brushsize = 6

def change_size_7():
    global brushsize
    brushsize = 7

def change_size_8():
    global brushsize
    brushsize = 8

def change_size_9():
    global brushsize
    brushsize = 9



turtle.getscreen().onkeypress(change_size_1 , "1")
turtle.getscreen().onkeypress(change_size_2 , "2")
turtle.getscreen().onkeypress(change_size_3 , "3")
turtle.getscreen().onkeypress(change_size_4 , "4")
turtle.getscreen().onkeypress(change_size_5 , "5")
turtle.getscreen().onkeypress(change_size_6 , "6")
turtle.getscreen().onkeypress(change_size_7 , "7")
turtle.getscreen().onkeypress(change_size_8 , "8")
turtle.getscreen().onkeypress(change_size_9 , "9")


def change_to_black():
    global brushcolor
    brushcolor = "black"

def change_to_green():
    global brushcolor
    brushcolor = "green"

def change_to_red():
    global brushcolor
    brushcolor = "red"

def change_to_yellow():
    global brushcolor
    brushcolor = "yellow"

def change_to_purple():
    global brushcolor
    brushcolor = "purple"

def change_to_orange():
    global brushcolor
    brushcolor = "orange"

def clear_page():
    turtle.clear()




turtle.getscreen().onkeypress(change_to_black , "b")
turtle.getscreen().onkeypress(change_to_green , "g")
turtle.getscreen().onkeypress(change_to_red , "r")
turtle.getscreen().onkeypress(change_to_yellow , "y")
turtle.getscreen().onkeypress(change_to_purple , "p")
turtle.getscreen().onkeypress(change_to_orange , "o")
turtle.getscreen().onkeypress(clear_page , "space")


    


turtle.getscreen().onkeypress(change_to_square , "s")
turtle.getscreen().onkeypress(change_to_circle , "c")


    



def drawShape(x,y):
    global brushtype
    if brushtype == "circle":
        draw_circle(x,y)

    if brushtype == "square":
        draw_square(x,y)


turtle.onscreenclick(drawShape, btn = 1, add = True)
    
   







turtle.getscreen().listen()
turtle.mainloop()



