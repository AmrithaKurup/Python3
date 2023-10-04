class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    def __str__(self):
        return f'{self.name} by {self.author}'
    def __len__(self):
        return self.price


b = Book('My Story', 'Amritha', 1000)
print(b)
print(len(b))
