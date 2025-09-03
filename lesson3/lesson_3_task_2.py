from smartphone import Smartphone

smartphone1 = Smartphone("Tecno", "POVA 7 Ultra 5G", "+71234567890")
smartphone2 = Smartphone("Samsung", "Galaxy S21", "+79123334956")
smartphone3 = Smartphone("Apple", "iPhone 15", "+79234567890")
smartphone4 = Smartphone("HUAWEI", "P60 Art", "+79123456789")
smartphone5 = Smartphone("Xiaomi", "Redmi 10А", "+79214567890")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for smartphone in catalog:
    print(f"Марка телефона: {smartphone.Brand} - Модель телефона: {smartphone.Model}. Номер телефона: {smartphone.Phone_number}")



