from tkinter import *

root = Tk()

Label(root, text = "Hello world").pack()

i = 0

# while - problem fixed

while i < 15:
  i += 2
  Label(root, text = str(i)).pack()

root.mainloop()
