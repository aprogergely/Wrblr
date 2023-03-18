import json
import tkinter as tk
import chat


class MyApp:
    def __init__(self):
        # open file that contains login details of all users        data protection hazard, needs to fix later
        # creates file if doesn't exist yet
        try:
            with open("logindata.json", "r") as f:
                data = json.load(f)
        except:
            with open("logindata.json", "x") as f:
                data = {'apro':'jelszo'}
                json.dump(data,f)

        self.username = ""
        self.password = ""

        # Create a new Tkinter window
        self.window = tk.Tk()
        self.window.title("Login")
        self.window.columnconfigure([0,1,2,3,4,5], minsize=30, weight=1)
        self.window.rowconfigure([0,1,2,3,4,5,6], minsize=30, weight=1)

        # Create a text box for username & password
        text_box_username = tk.Entry(self.window)
        text_box_password = tk.Entry(self.window)

        text_box_username.grid(row=2,column=2)
        text_box_password.grid(row=4,column=2)

        # Create a label for username & password
        label_username = tk.Label(text="Username:")
        label_password = tk.Label(text="Password:")

        label_username.grid(row=1,column=2)
        label_password.grid(row=3,column=2)

        # Create a button
        def on_button_click():
            # Retrieve the text from the text box
            with open("logindata.json", "r") as f:
                all_user_login_data = json.load(f)
            username = text_box_username.get()
            password = text_box_password.get()
            # Print the text to the console
            for entry in all_user_login_data:
                if entry == username:
                    if all_user_login_data[entry] == password:
                        savedaccount = open("account.txt", "w")
                        savedaccount.write(username)
                        savedaccount.close()
                        print("Login successful")
                        self.window.destroy()
                        chatwindow = chat.MyApp(username)
                        chatwindow.start()
                        break
                    else:
                        text_box_password.delete(0, tk.END)
                        raise Exception("Wrong password!")
            print("Not registered yet!")


        try_login_button = tk.Button(self.window, text="Submit", command=on_button_click)
        try_login_button.grid(row=6,column=2)

        # Start the main event loop of the window
    def start(self):
        self.window.mainloop()