import moduleP1 as dig

while True:
    print('We want to know the middle between two numbers!')
    name1 = int(input('First number: '))
    name2 = int(input('Second number: '))
    for name1,name2 in range (1,100):
        print(dig.numbers(name1, name2))
        break
    print('Try again!')









