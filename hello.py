from tkinter import*

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()

#myButton = Button(root, text="click Me!", state=DISABLED,padx=50, pady=50)
myButton = Button(root, text="click Me!",command =myClick)
myButton.pack()
#myLabel1 = Label(root, text="Hello World!").grid(row=0,column=0)
#myLabel2 = Label(root, text="my name is isaac").grid(row=1,column=5)

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=10)

root.mainloop()
