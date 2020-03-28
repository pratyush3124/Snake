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

        for i in range(10):
            for j in range(10):
                self.create_rectangle(i*30, j*30, 30*(i+1), 30*(j+1), fill = 'gray')

        self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'yellow')

                
        self.focus_set()
        self.bind('<Key>', self.changemove)

        self.direction = 'd'

        self.keepmoving()

    def move(self, dir):

        if dir == 'w':
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'gray')
            self.b -= 1
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'yellow')

        if dir == 'a':
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'gray')
            self.a -= 1
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'yellow')

        if dir == 's':
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'gray')
            self.b += 1
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'yellow')

        if dir == 'd':
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'gray')
            self.a += 1
            self.create_rectangle(self.a*30, self.b*30, 30*(self.a+1), 30*(self.b+1), fill = 'yellow')

    def changemove(self, event):
        self.direction = event.char

    def keepmoving(self):
        self.move(self.direction)
        self.parent.after(300, self.keepmoving)

app = Snake()
app.mainloop()

