import chat
import registering
import tkinter as tk


#window = tk.Tk()
#window.title("Loading...")

#def load(event):
    #nextwindow=""
    #window.destroy()
try:
        savedaccount = open("account.txt", "r")
        nextwindow = chat.MyApp(savedaccount.readline())
        nextwindow.start()
except:
        nextwindow = registering.MyApp()
        nextwindow.start()

#window.bind("<Key>", load)

#window.mainloop()