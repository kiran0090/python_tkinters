from tkinter import *

root = Tk()

myLabel1 =Label(root, text='hello world!') #creating a label widget
myLabel2 =Label(root, text='My name kiran.')

myLabel1.grid(row=0, column=0) #showing it onto the screen
myLabel2.grid(row=1, column=5)

root.mainloop()