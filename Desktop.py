from tkinter import Tk, Label

dsk = Tk()
dsk.title("pyapp")
dsk.geometry("600x500")
dsk.maxsize(600, 500)
dsk.minsize(300, 300)
label1 = Label(
    text="welcome to my app",
    bg="red",
    fg="yellow",
    font="helvetica 30 bold",
    padx="50",
    pady="50",
)
# label1.pack(side=LEFT,fill="x")
label1.pack(fill="x")
dsk.config(background="cyan")
dsk.mainloop()
