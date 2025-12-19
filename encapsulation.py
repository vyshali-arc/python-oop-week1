class UserLogin:
    def __init__(self, username, password):
        self.username = username         
        self.__password = password        

    def login(self, entered_password):
        if entered_password == self.__password:
            print("Login successful")
        else:
            print("Invalid password")

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password changed successfully")
        else:
            print("Old password is incorrect")

user = UserLogin("vyshali", "mypassword123")

user.login("wrongpass")
user.login("mypassword123")

user.change_password("mypassword123", "newpass456")
user.login("newpass456")
