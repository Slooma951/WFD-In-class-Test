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

phone1 = Phone("iPhone", "13", 2021, 799, "Midnight Black")

phone1.display_info()

phone1.update_price(600)
phone1.update_colour("Pink")
phone1.display_info()
