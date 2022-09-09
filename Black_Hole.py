import tkinter as tk
root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()
canvas2= tk.Canvas(root, width=400, height=200, relief='raised')
canvas2.pack()
canvas3= tk.Canvas(root, width=400, height=200, relief='raised')
canvas3.pack()
label1 = tk.Label(root, text='Black Holes and Dwarf Stars')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
label2 = tk.Label(root, text='Enter the mass of the star:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
def star():
    x1 = entry1.get()
    G = 6.67 * 10 ** -11
    c_sq = 9 * 10 ** 16
    M = float(x1) * 2 * 10 ** 30
    r = (2 * G * M) / (c_sq)
    if float(x1)<=0:
        e3 = tk.Label(root, text='Invalid Input!', font=('helvetica', 10,'bold'))
        canvas1.create_window(200, 250, window=e3)
    if float(x1) >= 1.4:
        l9 = tk.Label(root, text='It turns out to be a Blackhole!',font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 100, window=l9)
        label3 = tk.Label(root, text='The radius of Black Hole is:', font=('helvetica', 10))
        canvas1.create_window(200, 200, window=label3)
        label4 = tk.Label(root, text=str(r / 1000) + 'km', font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 220, window=label4)
        if float(x1)>=10**5:
            b1 = tk.Label(root, text='The type of black hole is Supermassive black hole', font=('helvetica', 10))
            canvas1.create_window(200, 250, window=b1)   
        elif float(x1) in range (10**3,100001):
            b2 = tk.Label(root, text='The type of black hole is Intermediate black hole', font=('helvetica', 10))
            canvas1.create_window(200, 250, window=b2)
        elif float(x1) in range(10,1001):
            b3 = tk.Label(root, text='The type of black hole is Stellar black hole', font=('helvetica', 10))
            canvas1.create_window(200, 250, window=b3)
        l2 = tk.Label(root, text='Enter the desired velocity:')
        l2.config(font=('helvetica', 10))
        canvas2.create_window(200, 100, window=l2)
        e1 = tk.Entry(root)
        canvas2.create_window(200, 140, window=e1)
        def getvelocity():
            x2=e1.get()
            V=((2*G*M*1000)/r)**(1/2)
            if float(x2) > V:
               label5 = tk.Label(root, text='sucessful return!', font=('helvetica', 10, 'bold'))
               canvas2.create_window(200, 210, window=label5)
            else:
               label6 = tk.Label(root, text='no return!', font=('helvetica', 10, 'bold'))
               canvas2.create_window(200, 210, window=label6) 
        button2 = tk.Button(text='Find out more ?', command=getvelocity, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas2.create_window(200, 180, window=button2)
        l12 = tk.Label(root, text='Enter the desired angle in terms of degrees:')
        l12.config(font=('helvetica', 10))
        canvas3.create_window(200, 100, window=l12)
        e2 = tk.Entry(root)
        canvas3.create_window(200, 140, window=e2)
        def getangle():
            x3=e2.get()
            b=90
            if float(x3)==b:
                label15 = tk.Label(root, text='can escape!', font=('helvetica', 10, 'bold'))
                canvas3.create_window(200, 165, window=label15)
            if float(x3)>b:
                z1 = tk.Label(root, text='no escape!', font=('helvetica', 10, 'bold'))
                canvas3.create_window(200, 165, window=z1)
            if float(x3)>=0 and float(x3)<90 :
                label16 = tk.Label(root, text='no escape!', font=('helvetica', 10, 'bold'))
                canvas3.create_window(200, 165, window=label16)
        button3 = tk.Button(text='Find out more ?', command=getangle, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        canvas3.create_window(200, 200, window=button3)
    if float(x1)>0 and float(x1)<1.4:
        l10 = tk.Label(root, text='It turns out to be a Dwarf star!',font=('helvetica', 10, 'bold'))
        canvas1.create_window(200, 100, window=l10)
        M = float(x1) * 2 * 10 ** 30
        R = 1 / (M ** 1 / 3)
        G = 6.67 * (10 ** -11)
        E = (G * M) / R
        label10 = tk.Label(root, text='The radius of Dwarf Star is:', font=('helvetica', 10))
        canvas1.create_window(200,200, window=label10)
        label11 = tk.Label(root, text=str(R) + 'km', font=('helvetica', 10, 'bold'))
        canvas1.create_window(200,230, window=label11)
        label12 = tk.Label(root, text='The potential energy of Dwarf Star is:', font=('helvetica', 10))
        canvas1.create_window(200,260, window=label12)
        label13 = tk.Label(root, text=str(E) + 'joules', font=('helvetica', 10, 'bold'))
        canvas1.create_window(200,290, window=label13)
button1 = tk.Button(text='Find out more ?', command=star, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()
