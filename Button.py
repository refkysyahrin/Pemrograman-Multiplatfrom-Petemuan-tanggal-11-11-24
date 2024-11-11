import tkinter
import tkinter.messagebox
top = tkinter.Tk()
def helloCallBack():
    tkinter.messagebox.showinfo ( "Hello Python", "Hello World")
B = tkinter.Button(top, text ="Selamat Datang", command =helloCallBack)
B.pack()
top.mainloop()