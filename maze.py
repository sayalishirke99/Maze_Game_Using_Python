import turtle
from random import randint
import pyglet
from pyglet.window import key
import math
from tkinter import *
from tkinter import messagebox
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from PIL import Image
import sys
from PIL import ImageTk
import os
from pyglet.window import mouse
import Image
root = Tk()
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
from pyglet import clock
def submit():
    import turtle
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Dare Maze")
    wn.setup(700, 700)

    # register shapes
    #turtle.register_shape("C:/Users/sayali shirke/Desktop/submission/tenor")
    #turtle.register_shape("wizard_left.gif")
    #turtle.register_shape("treasure.gif")
    #turtle.register_shape("wall.gif")

    # Create Pen
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("white")
            self.penup()
            self.speed(-50)

    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("blue")
            self.penup()
            self.speed(-50)
            self.gold = 0

        def go_up(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor() + 24
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_down(self):
            move_to_x = player.xcor()
            move_to_y = player.ycor() - 24
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_left(self):
            move_to_x = player.xcor() - 24
            move_to_y = player.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def go_right(self):
            move_to_x = player.xcor() + 24
            move_to_y = player.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)

        def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 5:
                return True
            else:
                return False

    class Treasure(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    levels = [""]
    level_1 = [
        "P                   XXXXX",
        "XXXXXX  XXXXXXXXXX  XX  X",
        "X        XXXT          XX",
        "XXXXXTXX XXXXX XXXXX  XXX",
        "XXXX     XXXXXXXXXXXXXXXX",
        "XXXXXXX X           TX XX",
        "XXXXXX  XXXXXXXXXX  XXXXX",
        "XXXXXX  XXXXXXXXXX  XXXXX",
        "X                   XXXXX",
        "XXXXXXX                XX",
        "XXX       XXXXX XX XXXXXX",
        "XXT  XXX  XXXXX XX XX  XX",
        "XXX  XXXXXXXXXX XX XXXX X",
        "XXX               XXXXXXX",
        "XXXXXXX  XX XXX      TXXX",
        "XXXXXXX XXXXXXXXXXXXXXXXX",
        "XXXXXXX   XXXXX XXXXXXXXX",
        "XXX       XXXXXXXXXXXXXXX",
        "XXXXXXX   XXXXXXXXXXXXXXX",
        "XXXXXXX           XXXXXXX",
        "XXXXXXX XXXXXXXX  XXXXXXX",
        "XXXXXXXTXXXXXXXX XXXXXXXX",
        "XXXXXXX XXXXXXXX XXXXXXXX",
        "XXXXXXXXXXXXXXXX  XXXXXXX"
    ]

    level_2 = [
        "XXPXXXXXXXXXXXXXXXXXXXXXX",
        "X   XXXXXXXXXXXXXXXXXXX  ",
        "X   XX  X           XT   ",
        "X   X   X  XXXXXXXXXXX   ",
        "X          XXXXXXXXXXX X ",
        "XXXXXXX X              X ",
        "XXXXXX  XXXXXXXXXX XXXXX ",
        "XXXXXX XXXXXXXXXXX XXXXX ",
        "X       XX          XXXX ",
        "XXXXXXXXXXXXXXX XT XXXXX ",
        "XXX       XXXXX XX XXXXX ",
        "XX   XXX  XXXXX XX XX  XT",
        "XXX  XXXXXXXXXX XX XXXX  ",
        "XXX                XXXX  ",
        "XXXXXXXXXXXXXX  XX XXXXX ",
        "XXXXXXXX          XXXXXX ",
        "XXXXXXXX  XXXXX X XX     ",
        "XXXXXXXXX XXXXXXX XX XXXX",
        "XXXXXXXXX XXXXXXX XX XXXX",
        "XXXXXXXXX XXXXXXXTXX XXXX",
        "XXXXXXXXX XXXXXX      XXX",
        "XXXXXXXXX XXXXXXXXXXX XXX",
        "XXXXXXXT          XXX XXX",
        "XXXXXXXXXXXXXXXX  XXX XXX",
        "XXXXXXXXXXXXXXXXXXXXXT  X"
    ]

    level_3 = [
        "XXPXXXXXXXXXXXXXXXXXXXXXX",
        "X   XX  XXXXXXXXXX  XX  X",
        "X   XX  X           XX  X",
        "X   X   X  XXXXXXXXXXX  X",
        "X          XXXXXXXXXXX XX",
        "XXXXXXX X           TX XX",
        "XXXXXX  XXXXXXXXXX XXXXXX",
        "XXXXXX  XXXXXXXXXX XXXXXX",
        "X       XX          XXXXX",
        "XXXXXXX XXXXXXX XT XXXXXX",
        "XXX       XXXXX XX XXXXXX",
        "  T  XXX  XXXXX XX XX  XX",
        "XXX  XXXXXXXXXX XX XXXX X",
        "XXX                XXXX X",
        "XXXXXXXXXXXXXXT XX XXXXXX",
        "XXXXXXXX          XXXXXXX",
        "XXXXXXXX  XXXXX XXXXXXXXX",
        "X         XXXXXXXXXXXXXXX",
        "XXXXXXXX  XXXXXXXXXXXXXXX",
        "XXXXXXXX         XXXXXXXX",
        "X XXXXXT XXXXXXX  XXXXXXX",
        "XXXXXXXXXXXXXXXX  XXXXXXX",
        "XXXXXXXT XXXXXXX  XXXXXXX",
        "XXXXXXX           XXXXXXX",
        "XXXXXXX  XXXXXXXXXXXXXXXX"
    ]

    treasures = []

    if var.get() == "EASY":
        levels.append(level_1)
    elif var.get() == "MEDIUM":
        levels.append(level_2)
    else:
        levels.append(level_3)

    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                screen_x = -288 + (x * 24)
                screen_y = 288 - (y * 24)

                if character == "X":
                    pen.goto(screen_x, screen_y)
                    pen.shape("square")
                    pen.stamp()
                    walls.append((screen_x, screen_y))

                if character == "P":
                    player.goto(screen_x, screen_y)

                if character == "T":
                    treasures.append(Treasure(screen_x, screen_y))
    pen = Pen()
    player = Player()
    walls = []
    setup_maze(levels[1])


    # keybord binding says that
    turtle.listen()
    turtle.onkey(player.go_left, "Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_up, "Up")
    turtle.onkey(player.go_down, "Down")
    wn.tracer(0)

    while True:
        for treasure in treasures:
            if player.is_collision(treasure):
                player.gold += treasure.gold
                print("player gold: {}".format(player.gold))
                treasure.destroy()
                treasures.remove(treasure)
                if player.gold == 600:
                    print("the game is over")
                    window = Tk()
                    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
                    window.withdraw()
                    messagebox.showinfo('DARE MAZE', 'CONGRALUTIONS')
                    window.deiconify()
                    window.destroy()
                    window.quit()
                    turtle.bye()

        wn.update()

    while True:
        pass
    return locals()


frame = Frame(root)
frame.pack()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack()
root.minsize(width=800, height=600)
label1 = Label(frame, text="WELCOME TO DARE MAZE", justify="center", fg='white', bg='black', font=("Helvetica", 16))
label1.pack()
separator = Frame(frame1, height=5, width=800, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)
label2 = Label(frame2, text="ENTER YOUR NAME", font=("Times", 14, "bold"), fg="black", height=0)
label2.pack(side=LEFT)
t1 = Entry(frame2)
t1.pack()
b1 = Button(frame5, text="Quit", fg='white', bg='black', command=root.destroy, font=16)
b1.pack(side="bottom")
var = StringVar(root)
var.set('EASY')
w = OptionMenu(frame3, var, "EASY", "MEDIUM", "DIFFICULT")
w.pack(side=RIGHT)
lab = Label(frame3, text="ENTER LEVEL", font=("Times", 14, "bold"), fg="black", height=0)
lab.pack()
b2 = Button(frame4, text="Submit", fg='white', bg='black', command=submit, font=16)
b2.pack()

window = pyglet.window
animation = pyglet.image.load_animation("C:/Users/sayali shirke/Desktop/submission/tenor.gif")
animeSprite = pyglet.sprite.Sprite(animation)

w = animeSprite.width
h = animeSprite.height
window = pyglet.window.Window(500, 350)
x, y = window.get_location()
window.set_location(x + 5, y + 1)
r, g, b, alpha = 0.5, 0.5, 0.8, 0.5
pyglet.gl.glClearColor(r, g, b, alpha)


@window.event
def on_draw():
    window.clear()
    animeSprite.draw()
    main_batch.draw()


def update(dt):
    running = True


if __name__ == '__main__':
    main_batch = pyglet.graphics.Batch()
    score_label = pyglet.text.Label(text='DARE MAZE', x=100, y=200, batch=main_batch, font_size=25, font_name='Matura MT Script Capitals')


def on_key_press(symbol, modifiers):
   if symbol == key.ENTER:
      has_exit = True


pyglet.app.run()

width = 440
height = 365


def showimg(self):
    try:
        img = Image.open("C:/Users/sayali shirke/Desktop/submission/maze.jpg")
    except IOError:
        pass


gallo = Image.open("C:/Users/sayali shirke/Desktop/submission/images.jpg")
image2 = gallo.resize((width, height), Image.NEAREST)
galloing = ImageTk.PhotoImage(image2)
panel = Label(frame4, image=galloing)
panel.pack(side="bottom")
frame4.mainloop()
root.mainloop()


