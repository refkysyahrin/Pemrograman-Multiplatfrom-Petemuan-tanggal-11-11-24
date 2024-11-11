import tkinter as tk

master = tk.Tk()

w = tk.Spinbox(master, from_=0, to=10)
w.pack()

master.mainloop()
