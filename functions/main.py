def say_hello():
    print('hello')

say_hello()
print("------------------------")
def say_name(name):
    print(f'My name is {name}')

say_name('Amritha')
say_name('Shantanu')
say_name('Chiu')

print("------------------------")
def calc(a,b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')

calc(4,2)
print("------------------------")
def sum(a,b):
    c = a+b
    return c

d = sum(1,2)
print(d)
