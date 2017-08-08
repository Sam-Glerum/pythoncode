import sys
import Tkinter

top = Tkinter.Tk()

def hello():
    print("Hello")
Tkinter.Canvas(top, bg='red').grid()
Tkinter.Button(top, text='test', bg='blue', command=hello).grid()
# Tkinter.Button(top, text='Woho!', command=top.destroy).pack()
top.mainloop()
