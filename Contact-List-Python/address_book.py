"""
Made By: - Vansh Sachdeva

Github Profile Name: - Mr Arthor



"""
from tkinter import *

root = Tk()
root.geometry('400x600')
root.config(bg = 'Salmon')
root.title('Contact List')
root.resizable(0,0)
contactlist = [
    ['Maheswari',  '0176738493',' 1','1 '],
    [' Sharma',  '2684430000',' 1','1 '],
    ['Kabra',   '4338354432',' 1','1 '],
    ['Modi','6834552341',' 1','1 '],
    ['kaushik',   '1234852689',' 1','1 '],
    ['Shaa' , '2119876543',' 1','1 '],
    ]

Name = StringVar()
Number = StringVar()
EmailId = StringVar()
Address= StringVar()

#create frame
Form = Frame(root)
Form.pack(side = RIGHT)

ScrollBar = Scrollbar(Form, orient=VERTICAL)
Select = Listbox(Form, yscrollcommand=ScrollBar.set, height=12)
ScrollBar.config (command=Select.yview)
ScrollBar.pack(side=RIGHT, fill=Y)
Select.pack(side=LEFT,  fill=BOTH, expand=1)



def Selected():
    return int(Select.curselection()[0])
    
def AddContact():
    contactlist.append([Name.get(), Number.get(),EmailId.get(),Address.get()])
    Select_set()

def EDIT():
    contactlist[Selected()] =[Name.get(), Number.get(),EmailId.get(),Address.get()]
    Select_set()
    
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
def VIEW():
    NAME, PHONE ,email,address= contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    EmailId.set(email)
    Address.set(address)


def EXIT():
    root.destroy()

def RESET():
    Name.set('')
    Number.set('')


def Select_set() :
    contactlist.sort()
    Select.delete(0,END)
    for name,phone,email,Address in contactlist :
        Select.insert (END, name)
Select_set()



Label(root, text = 'Name', font='arial 12 bold', bg = 'White').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 160, y=20)
Label(root, text = 'Phone No', font='arial 12 bold',bg = 'White').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 160, y=70)
Label(root, text = 'Email Address', font='arial 12 bold', bg = 'White').place(x= 30, y=110)
Entry(root, textvariable = EmailId).place(x= 160, y=110)
Label(root, text = 'Address', font='arial 12 bold',bg = 'white').place(x= 30, y=150)
Entry(root, textvariable = Address).place(x= 160, y=150)

Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 50, y=210)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 50, y=250)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 50, y=290)
Button(root,text="VIEW", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 50, y=330)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 300, y=420)
Button(root,text="RESET", font='arial 12 bold',bg='SlateGray4', command = RESET).place(x= 50, y=370)


root.mainloop()
  
