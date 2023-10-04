import random


def rand_num(low, high, n):
    for c in range(0, n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 5):
    print(num)
