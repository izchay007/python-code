from tkinter import*

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter your name: ")

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.insert(0,str(current) + str(number))

#Define buttons
button1 = Button(root,text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root,text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root,text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root,text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root,text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root,text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root,text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root,text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root,text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root,text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root,text="+", padx=40, pady=20, command=lambda: button_click)
button_equal = Button(root,text="=", padx=40, pady=20, command=lambda: button_click)
button_clear = Button(root,text="Clear", padx=40, pady=20, command=lambda: button_click)

#Put buttons on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
#button_add.grid(row=4,column=0)
#button_equal.grid(row=4,column=0)
#button_clear.grid(row=4,column=0)

root.mainloop()