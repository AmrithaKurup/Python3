try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print('Denominator cant be zero')
finally:
    print('All done')
