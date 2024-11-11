import tkinter as tk

root = tk.Tk()

labelframe = tk.LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")

left = tk.Label(labelframe, text="Inside the LabelFrame")
left.pack()

root.mainloop()
