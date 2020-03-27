from tkinter import *
from random import randint

root = Tk()
root.geometry('300x300')

a = randint(0,9)
b = randint(0,9)

def move(event):
    global a,b
    if event.char == 'w':
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'gray')
        b -= 1
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'yellow')

    if event.char == 'a':
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'gray')
        a -= 1
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'yellow')

    if event.char == 's':
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'gray')
        b += 1
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'yellow')

    if event.char == 'd':
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'gray')
        a += 1
        pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'yellow')


pg = Canvas(root, width = 300, height = 300)
pg.focus_set()
pg.bind('<Key>', move)


for i in range(10):
    for j in range(10):
        pg.create_rectangle(i*30, j*30, 30*(i+1), 30*(j+1), fill = 'gray')


pg.create_rectangle(a*30, b*30, 30*(a+1), 30*(b+1), fill = 'yellow')

pg.pack()

root.mainloop()
