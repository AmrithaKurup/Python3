class Car:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color

    def start(self):
        return (self.model + 'Engine started')


car1 = Car('Hyundai', 10000, 'Yellow')
print(car1.start())
