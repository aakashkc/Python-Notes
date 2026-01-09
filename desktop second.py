from tkinter import *
dsk=Tk()
dsk.title("this is title")
dsk.geometry("400x400")
dsk.minsize(10,10)
dsk.maxsize(700,700)
label2=Label(text="Name",bg="red",fg="blue",font="sans-serief 40 bold",padx="50",pady="50")

label2.pack()
dsk.config(background="blue")
name=Entry(text="Enter you name")

name.pack(padx="40",pady="40")





dsk.mainloop()