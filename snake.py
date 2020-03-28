from tkinter import Canvas, Tk
from random import randint


class Snake(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('300x300')

        self.canvas = Grid(self)
        self.canvas.pack()

class Grid(Canvas):
    def __init__(self, parent):
        self.parent = parent

        Canvas.__init__(self, parent, width = 300, height = 300)

        # self.a = randint(0,9)
        # self.b = randint(0,9)

        self.a = 4
        self.b = 4

        for i in range(15):
            for j in range(15):
                self.create_rectangle(i*20, j*20, 20*(i+1), 20*(j+1), fill = 'gray')

        self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'yellow')

                
        self.focus_set()
        self.bind('<Key>', self.changemove)

        self.direction = 'a'

        self.keepmoving()



    def move(self, dir):

        if dir == 'w':
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'gray')
            self.b -= 1
            self.outside()
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'yellow')

        if dir == 'a':
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'gray')
            self.a -= 1
            self.outside()
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'yellow')

        if dir == 's':
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'gray')
            self.b += 1
            self.outside()
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'yellow')

        if dir == 'd':
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'gray')
            self.a += 1
            self.outside()
            self.create_rectangle(self.a*20, self.b*20, 20*(self.a+1), 20*(self.b+1), fill = 'yellow')

    def changemove(self, event):
        self.direction = event.char

    def keepmoving(self):
        self.move(self.direction)
        self.parent.after(300, self.keepmoving)

    def outside(self):
        if self.a not in range(15):
            if self.a > 5:
                self.a -=15
            elif self.a < 5:
                self.a +=15
        
        if self.b not in range(15):
            if self.b > 5:
                self.b -=15
            elif self.b < 5:
                self.b +=15

app = Snake()
app.mainloop()

