class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def do_something(self):
        print("Hi " + self.name)

    def __str__(self):
        return self.name + " " + self.email


users = [User("Ali Can", "ali@gmail.com"), User("Veli Can", "veli@gmail.com")]

for user in users:
    user.do_something()
