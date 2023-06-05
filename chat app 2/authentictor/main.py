from authenticator import *


class Authenticate():
    def __init__(self, iohandler: IIOHandler, 
                 databasehandler: IDatabaseHandler, 
                 authenticator: IAuthenticator) -> None:
        
        self.iohandler=iohandler
        self.databasehandler=databasehandler
        self.authenticator=authenticator

    def authenticate(self):
        self.iohandler.write_output("Kérlek add meg a felhasználónevedet!")
        userName = self.iohandler.read_input()

        self.iohandler.write_output("Kérlek add meg a jelszavadat!")
        passWord = self.iohandler.read_input()

        result = self.authenticator.authenticate(userName, passWord)

        if result:
            self.iohandler.write_output("Beengedtem")
        else:
            self.iohandler.write_output("Nem engedtem be")


iohandler = IOHandler()
databasehandler = DatabaseHandler()
authenticatorObject = Authenticator()

authenticate = Authenticate(iohandler, databasehandler, authenticatorObject)
authenticate.authenticate()


