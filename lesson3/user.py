class User:
    def __init__(self, first_name, last_name):
        print("Создан")
        self.first_Name = first_name
        self.last_Name = last_name

    def first_name(self):
        print("Моё имя", self.first_Name)

    def last_name(self):
        print("Моя фамилия", self.last_Name)

    def first_Last_Name(self):
        print("Меня зовут", self.first_Name, self.last_Name)





