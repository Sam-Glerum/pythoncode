import Tkinter

top = Tkinter.Tk()


Tkinter.Canvas(top, bg='red').grid()
Tkinter.Button(top, text='test', bg='blue').grid()
# Tkinter.Button(top, text='Woho!', command=top.destroy).pack()
top.mainloop()
