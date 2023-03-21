import json
import tkinter as tk
import login

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
        self.window.title("Register")
        self.window.columnconfigure([0,1,2,3], minsize=30, weight=1)
        self.window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize=30, weight=1)

        #frame = tk.Frame(window, relief=tk.RIDGE, borderwidth=5)
        #frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # Create a text box for username & password
        text_box_username = tk.Entry(self.window)
        text_box_password = tk.Entry(self.window)

        text_box_username.grid(row=2,column=2)
        text_box_password.grid(row=4,column=2)

        # Create a label for username & password
        label_username = tk.Label(self.window, text="Username:")
        label_password = tk.Label(self.window, text="Password:")
        label_login = tk.Label(self.window, text="Already have an account?")

        label_username.grid(row=1,column=2)
        label_password.grid(row=3,column=2)
        label_login.grid(row=7,column=2)

        # Create a button used to submit login details
        def on_button_click():
            # Retrieve the text from the text box
            with open("logindata.json", "r") as f:
                all_user_login_data = json.load(f)
            username = text_box_username.get()
            password = text_box_password.get()
            # Print the text to the console
            try:
                all_user_login_data[username]
                print("User already exists!")
            except:
                if len(username)>2 & len(username)<21:
                    if len(password)>7 & len(password)<51:
                        all_user_login_data[username]=password
                        with open("logindata.json", "w") as f:
                            json.dump(all_user_login_data,f)
                        print("Account creation successful!")
                    else:
                        print("Password needs to be between 8 and 50 characters long!")
                else:
                    print("Username needs to be between 3 and 20 characters long!")

        def go_to_login():
            self.window.destroy()
            loginwindow = login.MyApp()
            loginwindow.start()

        try_register_button = tk.Button(self.window, text="Submit", command=on_button_click)
        try_register_button.grid(row=5,column=2)

        login_button = tk.Button(self.window, text="Log in!", command=go_to_login)
        login_button.grid(row=8,column=2)
        # Start the main event loop of the window
    def start(self):
        self.window.mainloop()