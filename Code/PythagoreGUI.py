from tkinter import *
from math import sqrt
root=Tk()
root.title("Calculatrice Théorème de Pythagore")
root.iconbitmap(default='Logo.ico')
root.geometry('500x150')
root.configure(background='white')

f1=Frame(root, width=500, height=150)
f1.pack()
f2=Frame(root, width=500, height=150)
f2.pack()

var_a=StringVar()
var_b=StringVar()
var_c=StringVar()

# Page d'accueil; ensuite demande quel côté résoudre
def start():
    welcome_label=Label(f1, text="Bienvenue sur la calculatrice de Pythagore", fg="#3333ff",font=("Arial", 16))
    solve_for=Label(f1, text="Quel côté est l'inconnu A, B, ou C ?",font=("Arial", 14))
    button_a=Button(f2, text="Pour A", font=("Arial", 16) , fg="#333399", command = solve_a, height = 1, width = 5,relief=RAISED)
    button_b=Button(f2, text="Pour B", font=("Arial", 16), fg="#333399", command = solve_b, height = 1, width = 5,relief=RAISED)
    button_c=Button(f2, text="Pour C",font=("Arial", 16), fg="#333399", command = solve_c,height = 1, width = 5,relief=RAISED)

    welcome_label.pack()
    solve_for.pack()
    button_a.pack(side=LEFT)
    button_b.pack(side=LEFT)
    button_c.pack(side=LEFT)


# Math, labels, buttons, and frames to solve for A
def solve_a():
    f1.pack_forget()
    f2.pack_forget()
    new_frame=Frame(root)
    new_frame.pack()

    def ans_a():
        new_frame.pack_forget()
        new_frame1=Frame(root)
        new_frame1.pack()
        value_b=float(var_b.get())
        value_c=float(var_c.get())
        a=sqrt((value_c**2)-(value_b**2))
        ans=Label(new_frame1, text=("La valeur de A est : "+str(a)))
        ans.pack()


    label_b=Label(new_frame, text="Valeur de B:")
    label_c=Label(new_frame, text="Valeur de C:")
    e1=Entry(new_frame, textvariable=var_b)
    e2=Entry(new_frame, textvariable=var_c)
    submit=Button(new_frame, text="Calculer", fg="red", command=ans_a)

    label_b.grid(row=0, sticky=W)
    label_c.grid(row=1, sticky=W)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    submit.grid(row=2, column=1)



# Math, labels, buttons, and frames to solve for B
def solve_b():
    f1.pack_forget()
    f2.pack_forget()
    new_frame=Frame(root)
    new_frame.pack()

    def ans_b():
        new_frame.pack_forget()
        new_frame1=Frame(root)
        new_frame1.pack()
        value_a=float(var_a.get())
        value_c=float(var_c.get())
        b=sqrt((value_c**2)-(value_a**2))
        ans=Label(new_frame1, text=("La valeur de B est: "+str(b)))
        ans.pack()

    label_a=Label(new_frame, text="Valeur de A:")
    label_c=Label(new_frame, text="Valeur de C:")
    e1=Entry(new_frame, textvariable=var_a)
    e2=Entry(new_frame, textvariable=var_c)
    submit=Button(new_frame, text="Calculer", fg="red", command=ans_b)

    label_a.grid(row=0, sticky=W)
    label_c.grid(row=1, sticky=W)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    submit.grid(row=2, column=1)



# Math, labels, buttons, and frames to solve for C
def solve_c():
    f1.pack_forget()
    f2.pack_forget()
    new_frame=Frame(root)
    new_frame.pack()

    def ans_c():
        new_frame.pack_forget()
        new_frame1=Frame(root)
        new_frame1.pack()
        value_a=float(var_a.get())
        value_b=float(var_b.get())
        c=sqrt((value_a**2)+(value_b**2))
        ans=Label(new_frame1, text=("La valeur de C est: "+str(c)))
        ans.pack()

    label_a=Label(new_frame, text="Valeur de A:")
    label_b=Label(new_frame, text="Valeur de B:")
    e1=Entry(new_frame, textvariable=var_a)
    e2=Entry(new_frame, textvariable=var_b)
    submit=Button(new_frame, text="Calculer", fg="red", command=ans_c)

    label_a.grid(row=0, sticky=W)
    label_b.grid(row=1, sticky=W)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    submit.grid(row=2, column=1)




# Calls the initial welcome screen
start()
root.mainloop()
