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

        self.head = [0]*2

        self.head[0] = randint(0,9)
        self.head[1] = randint(0,9)

        b = self.head[0]
        a = self.head[1]-1
        self.tails = [(a,b)]

        self.apple = [0]*2

        for i in range(15):
            for j in range(15):
                self.create_rectangle(i*20, j*20, 20*(i+1), 20*(j+1), fill = 'gray')

        self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = 'yellow')
        self.create_rectangle(self.tails[0][0]*20, self.tails[0][1]*20, 20*(self.tails[0][0]+1), 20*(self.tails[0][1]+1), fill = 'orange')
        # self.create_rectangle(self.tails[1][0]*20, self.tails[1][1]*20, 20*(self.tails[1][0]+1), 20*(self.tails[1][1]+1), fill = 'orange')

        self.focus_set()
        self.bind('<Key>', self.changemove)

        self.direction = 's'

        self.createapple()

        self.keepmoving()

    def movehead(self, dir):
        
        self.movetails()

        if dir == 'w':
            self.head[1] -= 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = 'yellow')

        elif dir == 'a':
            self.head[0] -= 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = 'yellow')

        elif dir == 's':
            self.head[1] += 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = 'yellow')

        elif dir == 'd':
            self.head[0] += 1
            self.ifoutside()
            self.create_rectangle(self.head[0]*20, self.head[1]*20, 20*(self.head[0]+1), 20*(self.head[1]+1), fill = 'yellow')

        else:
            pass

        self.ifeaten()

    def movetail(self, object, behind):
        self.create_rectangle(behind[0]*20, behind[1]*20, 20*(behind[0]+1), 20*(behind[1]+1), fill = 'orange')
        return (behind[0], behind[1])

    def movetails(self):
        for i in range(len(self.tails)):
            if i == 0:
                self.create_rectangle(self.tails[i][0]*20, self.tails[i][1]*20, 20*(self.tails[i][0]+1), 20*(self.tails[i][1]+1), fill = 'gray')
            if i+1 not in range(len(self.tails)):
                self.tails[i] = self.movetail(self.tails[i], self.head)
            else:
                self.tails[i] = self.movetail(self.tails[i], self.tails[i+1])
            

    def addtail(self):
        a = self.tails
        b = [(self.tails[0][0], self.tails[0][1])] + a
        self.tails = b

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

    def createapple(self):
        a = randint(0,14)
        b = randint(0,14)
        c = 0
        for d in self.tails:
            if a == d[0] and b == d[1]:
                c += 1
        if a == self.head[0] and b == self.head[1]:
            c += 1
        if c > 0:
            self.createapple()
        else:
            self.create_rectangle(a*20, b*20, 20*(a+1), 20*(b+1), fill = 'red')
        
        self.apple[0], self.apple[1] = a,b


    def ifeaten(self):
        if self.head[0] == self.apple[0] and self.head[1] == self.apple[1]:
            self.createapple()
            self.addtail()

app = Snake()
app.mainloop()