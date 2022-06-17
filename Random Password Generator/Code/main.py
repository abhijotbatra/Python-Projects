from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.geometry("400x200")
root.resizable(0, 0)
root.title("Random Password Generator")
root.config(bg='LightSalmon')

heading = Label(root, text='PASSWORD GENERATOR',
                bg="LightSalmon", font='freestyle 15 bold').pack()
Label(root, text='Vansh Sachdev', font='freestyle 15 ',
      bg="LightSalmon").pack(side=BOTTOM)


pass_label = Label(root, text='PASSWORD LENGTH',
                   font='freestyle 10 bold', bg="LightSalmon").pack()
pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len,
                 width=15, bg="LightSalmon").pack()

pass_str = StringVar()


def Generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase)+random.choice(
            string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password+random.choice(string.ascii_uppercase +
                                          string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)


Button(root, text="GENERATE PASSWORD",
       command=Generator, bg="LightSalmon").pack(pady=5)
Entry(root, textvariable=pass_str, bg="LightSalmon").pack()


def Copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text='COPY TO CLIPBOARD',
       command=Copy_password, bg="LightSalmon").pack(pady=5)

root.mainloop()
