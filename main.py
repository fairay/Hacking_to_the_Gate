from tkinter import *

root = Tk()

Label(root, text = "Hello worl").pack()

i = []

while i < 15:
  i += 2
  Label(root, text = "i").pack()

root.mainloop()
