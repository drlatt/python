class  User():
    """simple class to define a user"""
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.occupation)

    def greet_user(self):
        print("Welcome " + self.first_name.title() + " " + self.last_name.title())

first_user = User('ken','oyewo','48','investment banker')

first_user.describe_user()
first_user.greet_user()
