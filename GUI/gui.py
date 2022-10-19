from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.eval('tk::PlaceWindow . center')
e = Entry(ventana, width=50)
e.pack()

def printText():
    print(e.get())

button = Button(ventana, text="submit",command=printText)
button.pack()
ventana.mainloop()

