import json

class IOHandler():
    ertek="g"
    def read_input():
        ertek=input("adjon meg egy valamit")

        print("a megadott érték: "+ertek)

    def write_output():
        ertek="g"
        print(ertek)

class IDatabaseHandler():
    def get_user_credentials(username):
        with open("logindata.json", "r") as f:
            all_user_login_data = json.load(f)
            try:
                print(all_user_login_data[username])
            except:
                    print("Username does not exist!")

class IAuthenticator():
    def authenticate(username,password):
        belepes=True
        with open("logindata.json", "r") as f:
            all_user_login_data = json.load(f)
            try:
                all_user_login_data[username]
                if all_user_login_data[username] == password:
                    belepes=True
                else: 
                    belepes=False
            except:
                belepes=False
            print(belepes)

        
IOHandler.read_input()
IOHandler.write_output()
IDatabaseHandler.get_user_credentials("John")
