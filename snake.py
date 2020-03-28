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

        # self.head[0] = randint(0,9)
        # self.head[1] = randint(0,9)

        self.head = [4,4, 'yellow']

        self.tail = [[1,4,'orange'],[2,4,'orange'],[3,4, 'orange']]

        for i in range(15):
            for j in range(15):
                self.create_rectangle(i*20, j*20, 20*(i+1), 20*(j+1), fill = 'gray')

        self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = self.head[2])
        self.create_rectangle(self.tail[0][0]*20, self.tail[0][1]*20, 20*(self.tail[0][0]+1), 20*(self.tail[0][1]+1), fill = self.tail[0][2])
        self.create_rectangle(self.tail[1][0]*20, self.tail[1][1]*20, 20*(self.tail[1][0]+1), 20*(self.tail[1][1]+1), fill = self.tail[1][2])

        self.focus_set()
        self.bind('<Key>', self.changemove)

        self.direction = 's'

        self.keepmoving()

    def movehead(self, dir):
        self.movetails()

        if dir == 'w':
            self.head[1] -= 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = self.head[2])

        if dir == 'a':
            self.head[0] -= 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = self.head[2])

        if dir == 's':
            self.head[1] += 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = self.head[2])

        if dir == 'd':
            self.head[0] += 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = self.head[2])

    def movetail(self, object, behind):
        self.create_rectangle(behind[0]*20, behind[1]*20, 20*(behind[0]+1), 20*(behind[1]+1), fill = object[2])
        return behind[0], behind[1]

    def movetails(self):
        for i in range(len(self.tail)):
            if i+1 not in range(len(self.tail)):
                self.tail[i][0], self.tail[i][1] = self.movetail(self.tail[i], self.head)
            elif i == 0:
                self.create_rectangle(self.tail[i][0]*20, self.tail[i][1]*20, 20*(self.tail[i][0]+1), 20*(self.tail[i][1]+1), fill = 'gray')
                self.tail[i][0], self.tail[i][1] = self.movetail(self.tail[i], self.tail[i+1])    
            else:
                self.tail[i][0], self.tail[i][1] = self.movetail(self.tail[i], self.tail[i+1])

    def changemove(self, event):
        self.direction = event.char

    def keepmoving(self):
        self.movehead(self.direction)
        self.parent.after(250, self.keepmoving)

    def ifoutside(self):
        if self.head[0] not in range(15):
            if self.head[0] > 5:
                self.head[0] -=15
            elif self.head[0] < 5:
                self.head[0] +=15
        
        if self.head[1] not in range(15):
            if self.head[1] > 5:
                self.head[1] -=15
            elif self.head[1] < 5:
                self.head[1] +=15


app = Snake()
app.mainloop()

