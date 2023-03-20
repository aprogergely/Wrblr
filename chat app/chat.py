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
            with open("chathistory_0.json", "r") as f:
                chathistory = json.load(f)
        except:
            with open("chathistory_0.json", "w") as f:
                chathistory = {}
                json.dump(chathistory, f)

        self.username = username

        # Create a new Tkinter window
        self.window = tk.Tk()
        self.window.title("Chat")
        self.window.columnconfigure([0,1], minsize=70, weight=1)
        self.window.columnconfigure(2, minsize=300, weight=1)
        self.window.rowconfigure([0,1,2], minsize=50, weight=1)

        # create 2 frames used to separate the window into multiple parts
        frameL = tk.Frame(self.window, bg="red")
        frameR = tk.Frame(self.window, bg="yellow")
        frameL.grid(row=1,column=0,sticky=N+S)
        frameR.grid(row=1,column=2)
        frameL.columnconfigure([0,1], minsize=30, weight=1)
        frameR.columnconfigure([0,1,2], minsize=30, weight=1)
        frameL.rowconfigure(0, minsize=50, weight=1)
        frameL.rowconfigure([1,2,3], minsize=20, weight=1)
        frameR.rowconfigure([0,2,3], minsize=30, weight=1)
        frameR.rowconfigure(1, minsize=300, weight=1)
####
        #runs once upon opening the app and displays the global chat (every chat is global currently so the first one)
        # Create a Label at the top with the chatroom's name
        label_chatname = tk.Label(master=frameR, text="0")
        label_chatname.grid(row=0,column=2)

        # Create a text box for displaying chat history and another for inputtin new messages
        text_box_chat = tk.Text(master=frameR)
        entry_box = tk.Entry(master=frameR)

        text_box_chat.grid(row=1,column=2,sticky=W)
        entry_box.grid(row=2,column=2)

        for i in chathistory:
            text_box_chat.insert(tk.END, chathistory[i]["Name"]+"\n")
            text_box_chat.insert(tk.END, i[4:6]+"."+i[6:8]+" \n"+i[8:10]+":"+i[10:12]+" \n")
            text_box_chat.insert(tk.END, chathistory[i]["Text"]+"\n")
            text_box_chat.insert(tk.END, "\n")

        # Create a scrollbar for viewing ealier messages not vissible in the top textbox
        scrollbar = ttk.Scrollbar(master=frameR, orient=VERTICAL, command=text_box_chat.yview)
        scrollbar.grid(row=1,column=2,sticky=N+S+E)

        text_box_chat['yscrollcommand']=scrollbar.set

        # Create a button that sends the written text message when clicked
        def on_button_click():
            # Retrieve the text from the text box
            newtext = entry_box.get()
            x = datetime.datetime.now()
            # save newly wrote message in file
            microseconds=x.strftime("%Y"+"%m"+"%d"+"%H"+"%M"+"%S"+"%f")
            current_chatnumber=label_chatname["text"]
            with open("chathistory_"+str(current_chatnumber)+".json", "r") as f:
                chathistory = json.load(f)
            with open("chathistory_"+str(current_chatnumber)+".json", "w") as f:
                chathistory[microseconds]={}
                chathistory[microseconds]["Name"]=username
                chathistory[microseconds]["Text"]=newtext
                json.dump(chathistory,f)
            # send text message
            text_box_chat.insert(tk.END, username + "\n")
            text_box_chat.insert(tk.END, x.strftime("%H") + ":")
            text_box_chat.insert(tk.END, x.strftime("%M") + "\n")
            text_box_chat.insert(tk.END, newtext + "\n" + "\n")
            entry_box.delete(0, tk.END)


        post_comment_button = tk.Button(master=frameR, text="Submit", command=on_button_click)
        post_comment_button.grid(row=4,column=2)
####
        def Refresh_Chat_room(New_chatnumber=0, chatname="0"):
                #open new chat history
                with open("chathistory_"+str(New_chatnumber)+".json", "r") as f:
                    #chathistory = {}
                    chathistory = json.load(f)
                    
                # Change the Label at the top with the chatroom's name
                label_chatname["text"] = chatname

                #empty chatbox then fill it with new chaat history
                text_box_chat.delete('1.0', tk.END)
                for i in chathistory:
                    text_box_chat.insert(tk.END, chathistory[i]["Name"]+"\n")
                    text_box_chat.insert(tk.END, i[4:6]+"."+i[6:8]+" \n"+i[8:10]+":"+i[10:12]+" \n")
                    text_box_chat.insert(tk.END, chathistory[i]["Text"]+"\n")
                    text_box_chat.insert(tk.END, "\n")

        #Create a new button for every chatroom found and place it on a list on the left side
        i=0
        more_chatrooms = True
        while more_chatrooms == True:
            try:
                with open("chathistory_"+str(i)+".json", "r") as f:
                    open_chat_button = tk.Button(master=frameL, text=str(i))
                    open_chat_button.bind("<Button-1>", lambda event, x=i: Refresh_Chat_room(New_chatnumber=x,chatname=str(x)))
                    open_chat_button.grid(row=i,column=1,sticky=NW+SE)
                    i+=1
            except:
                more_chatrooms = False

        def New_Chat_room():
            with open("chathistory_"+str(i)+".json", "w") as f:
                create_new_history = {}
                json.dump(create_new_history, f)
                text_box_chat.delete('1.0', tk.END)
                #current_chatnumber = i
                new_chat_button.bind("<Button-1>", lambda event: Refresh_Chat_room(New_chatnumber=i,chatname=str(i)))
                new_chat_button.configure(text=i)


        new_chat_button = tk.Button(master=frameL, text="+")
        new_chat_button.bind("<Button-1>", lambda event: New_Chat_room())
        new_chat_button.grid(row=i,column=1,sticky=NW+SE)
        

    # Start the main event loop of the window
    def start(self):
        self.window.mainloop()