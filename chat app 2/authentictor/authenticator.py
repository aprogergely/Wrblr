import io

class IIOHandler:
    def read_input(self ) -> str:
        pass

    def write_output(self, output: str) -> None:
        pass


class IDatabaseHandler:
    def get_user_credentials(self, userName: str) -> str:
        pass


class IAuthenticator:
    def authenticate(self, userName: str, passWord: str) -> bool:
        pass


class IOHandler(IIOHandler):
    def read_input(self):
        result = input()
        return result
    
    def write_output(self, output):
        print(output)


class DatabaseHandler(IDatabaseHandler):
    def get_user_credentials(self, userName: str):

        database = "database.txt"

        with io.open(database, "r", encoding="utf-8") as file:
            for line in file:
                stored_username, password = line.strip().split(" ")
                if stored_username == userName:
                    return password
        return None
    

class Authenticator(IAuthenticator):
    def authenticate(self, userName: str, passWord: str):
        databaseHandler = DatabaseHandler()
        storedPassword = databaseHandler.get_user_credentials(userName)
        if storedPassword == passWord:
            return True
        else:
            return False