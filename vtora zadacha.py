class Car:
    def __init__(self, brand, model,  year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_des(self):
        print(self.brand.model.year)

c1 = Car("Volkswagen", "golf", "2021")
c2 = Car("Toyota", "RAV4", "2022")
