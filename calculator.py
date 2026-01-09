from tkinter import *
dsk=Tk()
dsk.title("Calculator")
dsk.geometry("400x450")
dsk.minsize(300,200)
dsk.maxsize(400,450)
def click(event):
    global entry_var
    text=event.widget.cget("text")
    # print(text)
    if text == "=":
        if entry_var.get().isdigit():
            values=int(entry_var.set())
        else:
            try:
                values=eval(entry_var.get())
            except Exception as a:
                print(a)
                entry_var.set("error")
                box.update()

                
            entry_var.set(values)
            box.update()
    elif text=="AC":
        entry_var.set("")
        box.update()
    else:
        entry_var.set(entry_var.get()+text)
        box.update()


entry_var=StringVar()
box=Entry(dsk,textvar=entry_var,font="sans-sarief 30 bold",fg="blue")
box.pack(fill=X, padx=10, pady=10)
frm=Frame(dsk, bg="orange")
butn1=Button(frm,text="1",bg="red",fg="white", padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="2",bg="red", fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="3",bg="red", fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="+",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="AC",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)


frm.pack(padx=5,pady=5)
frm=Frame(dsk, bg="orange")
butn1=Button(frm,text="4",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="5",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="6",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="-",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="X",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)




frm.pack( padx=5,pady=5)
frm=Frame(dsk, bg="orange")
butn1=Button(frm,text="7",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="8",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="9",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="/",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="off",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)




frm.pack( padx=5,pady=5)

frm=Frame(dsk, bg="orange")
butn1=Button(frm,text="0",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text=".",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT,)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="%",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="*",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)
butn1=Button(frm,text="=",bg="red",fg="white",padx=20,pady=20)
butn1.pack( padx=10, pady=5,side=LEFT)
butn1.bind("<Button-1>",click)

frm.pack(padx=5,pady=5)
dsk.config(background="orange")
dsk.mainloop()

