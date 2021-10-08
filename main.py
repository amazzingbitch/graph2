from tkinter import *
from random import randint

def ves(maska, peres):

    result = 0

    for i in range(3):
        for j in range(3):
            peres[i][j] = maska[i][j] * peres[i][j]
            result += peres[i][j]

    return result

def dd(maska):
    div = 0

    for i in range(3):
        for j in range(3):
            div += maska[i][j]

    return div

def drawing(event):
    global cnv, maska

    cnv.delete("all")
    x0 = 40
    y0 = 150
    constant = 110
    y = y0
    color = 'ff00ff'

    for i in range(3):
        x = x0
        for j in range(3):
            cnv.create_rectangle(x, y, x+constant, y+constant, outline='#e68b0b', fill='#7abf58')
            x +=constant
        y += constant

    x1 = randint(1, 380)
    if(x1 <= 40):
        y1 = randint(140, 200)
    else:
        y1 = 140

    y2 = randint(160, 490)
    if(y2 >= 470):
        x2 = randint(40, 380)
    else:
        x2 = 380

    cnv.create_line(x1, y1, x2, y2, fill='#bd88e3', width=3)

    peres = []

    for i in range(3):
        peres.append([])
        for j in range(3):
            peres[i].append([])
            peres[i][j] = 0

    if(abs(x2-x1) >= abs(y2 - y1)):
        len = abs(x2-x1)
    else:
        len = abs(y2-y1)

    dx = (x2 - x1)/len
    dy = (y2 - y1)/len

    x = x1
    y = y1

    i = 0

    while(i <= len):
        if(x >= 40 and x <= 150):
            if(y >= 150 and y <= 260):
                peres[0][0] = 1
            elif(y >= 260 and y <= 370):
                peres[1][0] = 1
            elif(y >= 370 and y <= 480):
                peres[2][0] = 1
        elif(x >= 150 and x <= 260):
            if (y >= 150 and y <= 260):
                peres[0][1] = 1
            elif (y >= 260 and y <= 370):
                peres[1][1] = 1
            elif (y >= 370 and y <= 480):
                peres[2][1] = 1
        elif(x >= 260 and x <= 370):
            if (y >= 150 and y <= 260):
                peres[0][2] = 1
            elif (y >= 260 and y <= 370):
                peres[1][2] = 1
            elif (y >= 370 and y <= 480):
                peres[2][2] = 1

        x += dx
        y += dy
        i += 1

    summ = ves(maska, peres)

    div = dd(maska)

    r = int('ff', 16) - ((int('ff', 16) * summ) // div)

    if(r <= int('f', 16)):
        r = '0' + str(hex(r)[2:])
    else:
        r = str(hex(r)[2:])

    color = '#' + r + 'ff' + r

    cnv.create_rectangle(400, 260, 500, 360, outline=color, fill=color)

    cnv.pack(fill=BOTH, expand=1)

def UpdateMaska(event):
    global maska
    global x_0_0, x_0_1, x_0_2, x_1_0, x_1_1, x_1_2, x_2_0, x_2_1, x_2_0

    maska[0][0] = int(x_0_0.get())
    maska[0][1] = int(x_0_1.get())
    maska[0][2] = int(x_0_2.get())

    maska[1][0] = int(x_1_0.get())
    maska[1][1] = int(x_1_1.get())
    maska[1][2] = int(x_1_2.get())

    maska[2][0] = int(x_2_0.get())
    maska[2][1] = int(x_2_1.get())
    maska[2][2] = int(x_2_2.get())

    div = 0

    for i in range(3):
        for j in range(3):
            div += maska[i][j]

    print(maska, div)

def Quiet(event):
    global draw
    global menu

    draw.destroy()
    menu.destroy()

#------------------------------------------------------------
draw = Tk()
draw.maxsize(600, 600)
draw.minsize(600, 600)
draw.title('Draw Window')

x = (draw.winfo_screenwidth() - draw.winfo_reqwidth()) / 2
y = (draw.winfo_screenheight() - draw.winfo_reqheight()) / 16
draw.wm_geometry("+%d+%d" % (x, y))

#------------------------------------------------------------

menu = Tk()
menu.maxsize(500, 500)
menu.minsize(500, 500)
menu.title('Menu')

x -= 600
menu.wm_geometry("+%d+%d" % (x, y))
#------------------------------------------------------------

btn_q = Button(menu, text='Quit')
btn_q.bind('<Button-1>', Quiet)
btn_q.place(x=450, y=450)

btn_update_maska = Button(menu, text='Update mask')
btn_update_maska.bind('<Button-1>', UpdateMaska)
btn_update_maska.place(x=100, y=200)

btn_draw = Button(menu, text='Draw')
btn_draw.bind('<Button-1>', drawing)
btn_draw.place(x=100, y=270)

label1 = Label(menu, text='Maska:')
label1.place(x=100, y=80)

x_0_0 = Entry(menu)
x_0_0.insert(0, '1')
x_0_0.place(x=100, y=100)

x_0_1 = Entry(menu)
x_0_1.insert(0, '2')
x_0_1.place(x=200, y=100)

x_0_2 = Entry(menu)
x_0_2.insert(0, '1')
x_0_2.place(x=300, y=100)

x_1_0 = Entry(menu)
x_1_0.insert(0, '2')
x_1_0.place(x=100, y=125)

x_1_1 = Entry(menu)
x_1_1.insert(0, '4')
x_1_1.place(x=200, y=125)

x_1_2 = Entry(menu)
x_1_2.insert(0, '2')
x_1_2.place(x=300, y=125)

x_2_0 = Entry(menu)
x_2_0.insert(0, '1')
x_2_0.place(x=100, y=150)

x_2_1 = Entry(menu)
x_2_1.insert(0, '2')
x_2_1.place(x=200, y=150)

x_2_2 = Entry(menu)
x_2_2.insert(0, '1')
x_2_2.place(x=300, y=150)
#------------------------------------------------------------

cnv = Canvas(draw)
div = 0
maska = []

for i in range(3):
    maska.append([])
    for j in range(3):
        maska[i].append([])

UpdateMaska(0)

menu.mainloop()
draw.mainloop()