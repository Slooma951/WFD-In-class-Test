class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Colour:", self.colour)

    def update_brand(self, new_brand):
        self.brand = new_brand

    def update_model(self, new_model):
        self.model = new_model

    def update_year(self, new_year):
        self.year = new_year

    def update_price(self, new_price):
        self.price = new_price

    def update_colour(self, new_colour):
        self.colour = new_colour

phone1 = Phone("Iphone", "13", 2021, 799, "midnight black")

phone1.display_info()

phone1.update_price(600)
phone1.update_colour("Pink")
phone1.display_info()
