from tkinter import *
from tkinter import messagebox
# importing the module 
from pytube import YouTube




#BUTTON COMMAND
def downloadVideo():
    link = e.get()
    yt = YouTube(link)
    yt.streams.get_highest_resolution().download()
<<<<<<< HEAD:GUI/gui.py
    mensaje = messagebox.showinfo("Status", "Video has been downloaded" )
=======
    messagebox.showinfo("Status", "Video has been downloaded" )
>>>>>>> 175e43f5f56599996bd44e0bf7c951c43a5b3134:video-downloader/video-downloader.py
    
    


#WINDOW
ventana = Tk()
ventana.geometry("400x400")
ventana.eval('tk::PlaceWindow . center')
ventana.title("Video Downloader")
ventana.configure(bg="#121212")

#YOUTUBE LOGO
imagen = PhotoImage(file="video-downloader/youtube_logo.png")
my_label = Label(ventana, image=imagen, bd=0)
my_label.place(relx=0.5, rely=0.4, anchor=CENTER)

#LABEL INSTRUCCIONS
my_label2 = Label(ventana, text="Put your link in the box below ⬇️")
my_label2.place(relx=0.5, rely=0.7, anchor=CENTER)

#INPUT BOX
e = Entry(ventana, width=30, border=3)
e.place(relx=0.5, rely=0.8, anchor=CENTER)




#SUBMIT BUTTON
button = Button(ventana, text="SUBMIT", activebackground="#234", command=downloadVideo)
button.place(relx=0.5, rely=0.9, anchor=CENTER)
ventana.mainloop()

#MessageBox



