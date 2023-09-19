
def p2():
    while True:
        name = input("what is your name ")
        if not name.isalpha():
            print('name can contain only alphabet letters, try again')
            name = ''
        else:
            break
    while True:
        age = input("what is your age ")
        if not age.isalnum():
            print('Age can contain only alphanumerical numbers, try again')
            age = ''
        elif int(age) < 0:
            print('Age can only be positive')
            age = ''
        else:
            break
    while True:
        height = input("what is your height in cm")
        if not height.isalnum():
            print('height can contain only alphanumerical numbers, try again')
        elif int(height) <= 30:
            print('Height must be higher than 30 ')
        elif int(height) >= 300:
            print('Height must be lower than 300 ')
        else:
            break
    print(f'So your name is {name}, you are {age} years old and {height} tall')


if __name__ == '__main__':
    p2()
