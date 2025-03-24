#A2
class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    #A3
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Colour:", self.colour)

    #A4
    def update_brand(self, new_brand):
        if isinstance(new_brand, str):
            self.brand = new_brand

    def update_model(self, new_model):
        if isinstance(new_model, str):
            self.model = new_model

    def update_year(self, new_year):
        if isinstance(new_year, int):
            self.year = new_year

    def update_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price

    def update_colour(self, new_colour):
        if isinstance(new_colour, str):
            self.colour = new_colour

#A5
class Smartphone(Phone):
    def __init__(self, brand, model, year, price, colour, os, storage):
        super().__init__(brand, model, year, price, colour)
        self.os = os
        self.storage = storage

    #A6
    def display_info(self):
        super().display_info()
        print("OS:", self.os)
        print("Storage:", self.storage, "GB")

    #A7
    def update_os(self, new_os):
        if isinstance(new_os, str):
            self.os = new_os

    def update_storage(self, new_storage):
        if isinstance(new_storage, int):
            self.storage = new_storage

#A8
phone1 = Phone("iPhone", "13", 2021, 799, "Midnight Black")
smartphone1 = Smartphone("Iphone", "15", 2023, 899, "green", "IOS17", 256)

#A9
phone1.display_info()
print("======================================")
smartphone1.display_info()
print("======================================")
#A10
phone1.update_price(600)
phone1.update_colour("Pink")

smartphone1.update_os("IOS 18")
smartphone1.update_storage(512)


phone1.display_info()
print("======================================")
smartphone1.display_info()
