class Usuarios:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}"