from tkinter import Canvas, Tk
from random import randint
from tkinter import messagebox



def keepmoving():
    global direction
    movehead(direction)
    if len(tails) < 20:
        Game.after(220, keepmoving)
    else:
        Game.after(220-(5*(len(tails)-20)), keepmoving)

def movehead(dir):
    if ifbit():
        return
    movetails()

    if dir == 'w':
        head[1] -= 1
        ifoutside()
        canvas.create_rectangle(
            head[0]*20, head[1]*20, 20*(head[0]+1), 20*(head[1]+1), fill='yellow')

    elif dir == 'a':
        head[0] -= 1
        ifoutside()
        canvas.create_rectangle(
            head[0]*20, head[1]*20, 20*(head[0]+1), 20*(head[1]+1), fill='yellow')

    elif dir == 's':
        head[1] += 1
        ifoutside()
        canvas.create_rectangle(
            head[0]*20, head[1]*20, 20*(head[0]+1), 20*(head[1]+1), fill='yellow')

    elif dir == 'd':
        head[0] += 1
        ifoutside()
        canvas.create_rectangle(
            head[0]*20, head[1]*20, 20*(head[0]+1), 20*(head[1]+1), fill='yellow')

    else:
        pass

    ifeaten()

def movetails():
    for i in range(len(tails)):
        if i == 0:
            canvas.create_rectangle(tails[i][0]*20, tails[i][1]*20, 20*(
                tails[i][0]+1), 20*(tails[i][1]+1), fill='gray')
        if i+1 not in range(len(tails)):
            tails[i] = moveit(tails[i], head)
        else:
            tails[i] = moveit(tails[i], tails[i+1])

def moveit(object, behind):
    canvas.create_rectangle(
        behind[0]*20, behind[1]*20, 20*(behind[0]+1), 20*(behind[1]+1), fill='orange')
    return (behind[0], behind[1])

def addtail():
    global tails
    a = tails
    b = [(tails[0][0], tails[0][1])] + a
    tails = b

def changemove(event):
    global direction
    x = head[0] - tails[len(tails)-1][0]
    y = head[1] - tails[len(tails)-1][1]

    if event.char == 'w' and y == 1:
        pass
    elif event.char == 's' and y == -1:
        pass
    elif event.char == 'a' and x == 1:
        pass
    elif event.char == 'd' and x == -1:
        pass
    else:
        direction = event.char

def ifoutside():
    if head[0] not in range(15):
        if head[0] > 5:
            head[0] -= 15
        elif head[0] < 5:
            head[0] += 15

    if head[1] not in range(15):
        if head[1] > 5:
            head[1] -= 15
        elif head[1] < 5:
            head[1] += 15

def createapple():
    a = randint(0, 14)
    b = randint(0, 14)
    c = 0
    for d in tails:
        if a == d[0] and b == d[1]:
            c += 1
    if a == head[0] and b == head[1]:
        c += 1
    if c > 0:
        createapple()
    else:
        canvas.create_rectangle(a*20, b*20, 20*(a+1), 20*(b+1), fill='red')

    apple[0], apple[1] = a, b

def ifeaten():
    if head[0] == apple[0] and head[1] == apple[1]:
        createapple()
        addtail()

def ifbit():
    if (head[0], head[1]) in tails:
        messagebox.showinfo('', 'You bit yourseves and died')
        return True

Game = Tk()
Game.geometry('300x300')

canvas = Canvas(Game,width=300, height=300)
canvas.pack()

head = [0]*2
head[0], head[1] = randint(0, 9), randint(0, 9)
tails = [(head[1]-1, head[0])]
apple = [0]*2

# grid
for i in range(15):
    for j in range(15):
        canvas.create_rectangle(
            i*20, j*20, 20*(i+1), 20*(j+1), fill='gray')

canvas.create_rectangle(head[0]*20, head[1]*20,
                        20*(head[0]+1), 20*(head[1]+1), fill='yellow')
canvas.create_rectangle(tails[0][0]*20, tails[0][1]*20, 20*(
    tails[0][0]+1), 20*(tails[0][1]+1), fill='orange')

canvas.focus_set()
canvas.bind('<Key>', changemove)

direction = 's'
createapple()
keepmoving()

Game.mainloop()