def ask():
    while True:
        try:
            x = int(input('Input an integer: '))
            result = x**2
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            print(f'Thank you, your number squared is: {result}')
            break


ask()
