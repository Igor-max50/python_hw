class Smartphone:
    def __init__(self, brand, model, phone_number):
    
        self.Brand = brand
        self.Model = model
        self.Phone_number = phone_number
    print("Список телефонов:")


    def brand(self):
        print(self.Brand)

    def model(self):
        print(self.Model)

    def phone_number(self):
        print(self.Phone_number)
