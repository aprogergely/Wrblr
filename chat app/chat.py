import json
import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk

class MyApp:
    def __init__(self, username):
        # open file that contains login details of all users        data protection hazard, needs to fix later
        # creates file if doesn't exist yet
        try:
            with open("chathistory.json", "r") as f:
                chathistory = json.load(f)
        except:
            with open("chathistory.json", "x") as f:
                chathistory = json.load(f)

        self.username = username

        # Create a new Tkinter window
        self.window = tk.Tk()
        self.window.title("Chat")

        # Create a text box for displaying chat history and another for inputtin new messages
        text_box_chat = tk.Text(self.window)
        text_box_entry = tk.Entry(self.window)

        text_box_chat.place(x=50, y=50, width=200, height=300)
        text_box_entry.place(x=50, y=400, width=200, height=30)

        for i in chathistory:
            text_box_chat.insert(tk.END, chathistory[i]["Name"]+"\n")
            text_box_chat.insert(tk.END, i+"\n")
            text_box_chat.insert(tk.END, chathistory[i]["Text"]+"\n")
            text_box_chat.insert(tk.END, "\n")

        # Create a scrollbar for viewing ealier messages not vissible in the textbox
        scrollbar = ttk.Scrollbar(self.window, orient=VERTICAL, command=text_box_chat.yview)
        scrollbar.place(x=300, y=50, width=20, height=300)

        text_box_chat['yscrollcommand']=scrollbar.set

        # Create a button
        def on_button_click():
            # Retrieve the text from the text box
            newtext = text_box_entry.get()
            x = datetime.datetime.now()
            # Print the text to the console
            chathistory[x.strftime("%f")]["Name"]=username
            chathistory[x.strftime("%f")]["Text"]=newtext
            with open("chathistory.json", "w") as f:
                json.dump(chathistory,f)
            text_box_chat.insert(tk.END, username + "\n")
            text_box_chat.insert(tk.END, x.strftime("%H") + ":")
            text_box_chat.insert(tk.END, x.strftime("%M") + "\n")
            text_box_chat.insert(tk.END, newtext + "\n" + "\n")
            text_box_entry.delete(0, tk.END)


        try_login_button = tk.Button(self.window, text="Submit", command=on_button_click)
        try_login_button.place(x=250, y=400, width=50, height=30)

        # Start the main event loop of the window
    def start(self):
        self.window.mainloop()