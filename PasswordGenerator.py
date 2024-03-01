import string
from tkinter import *
import random

def generator():
    small_letter = string.ascii_lowercase
    capital_letter = string.ascii_uppercase
    numbers = string.digits
    special_charecters = string.punctuation

    all=small_letter+capital_letter+numbers+special_charecters
    Password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_letter, Password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_letter+capital_letter, Password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all, Password_length))

root = Tk()
root.config(bg='gray20')
choice = IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(root,text='Password Generator', font=('times new roman', 20, 'bold'),bg='gray20', fg='white')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(pady=5)

length_Box=Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

generateButton=Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

root.mainloop()
