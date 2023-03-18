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
            with open("chathistory.json", "w") as f:
                chathistory = {}
                json.dump(chathistory, f)

        self.username = username

        # Create a new Tkinter window
        self.window = tk.Tk()
        self.window.title("Chat")
        self.window.columnconfigure([0,1], minsize=30, weight=1)
        self.window.columnconfigure(2, minsize=300, weight=1)
        self.window.rowconfigure([0,1,2], minsize=30, weight=1)

        # frames
        frameL = tk.Frame(self.window, bg="red")
        frameR = tk.Frame(self.window, bg="yellow")
        frameL.grid(row=1,column=1)
        frameR.grid(row=1,column=2)
        frameL.columnconfigure([0,1,2,3], minsize=30, weight=1)
        frameR.columnconfigure([0,1,2], minsize=30, weight=1)
        frameR.rowconfigure(1, minsize=300, weight=1)
        frameL.rowconfigure([0,1,2,3], minsize=30, weight=1)
        frameR.rowconfigure([0,2,3], minsize=30, weight=1)

        # Create a text box for displaying chat history and another for inputtin new messages
        text_box_chat = tk.Text(master=frameR)
        text_box_entry = tk.Entry(master=frameR)

        text_box_chat.grid(row=1,column=2,sticky=W)
        text_box_entry.grid(row=2,column=2)

        for i in chathistory:
            text_box_chat.insert(tk.END, chathistory[i]["Name"]+"\n")
            text_box_chat.insert(tk.END, i+"\n")
            text_box_chat.insert(tk.END, chathistory[i]["Text"]+"\n")
            text_box_chat.insert(tk.END, "\n")

        # Create a scrollbar for viewing ealier messages not vissible in the textbox
        scrollbar = ttk.Scrollbar(master=frameR, orient=VERTICAL, command=text_box_chat.yview)
        scrollbar.grid(row=1,column=2,sticky=N+S+E)

        text_box_chat['yscrollcommand']=scrollbar.set

        # Create a button
        def on_button_click():
            # Retrieve the text from the text box
            newtext = text_box_entry.get()
            x = datetime.datetime.now()
            # Print the text to the console
            microseconds=x.strftime("%f")
            chathistory[microseconds]={}
            chathistory[microseconds]["Name"]=username
            chathistory[microseconds]["Text"]=newtext
            with open("chathistory.json", "w") as f:
                json.dump(chathistory,f)
            text_box_chat.insert(tk.END, username + "\n")
            text_box_chat.insert(tk.END, x.strftime("%H") + ":")
            text_box_chat.insert(tk.END, x.strftime("%M") + "\n")
            text_box_chat.insert(tk.END, newtext + "\n" + "\n")
            text_box_entry.delete(0, tk.END)


        post_comment_button = tk.Button(master=frameR, text="Submit", command=on_button_click)
        post_comment_button.grid(row=4,column=2)

        # Start the main event loop of the window
    def start(self):
        self.window.mainloop()