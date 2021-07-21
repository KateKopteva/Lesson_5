while True:
    x, y = float(input('x= ')), float(input('y= '))
    sign = input('Знак операции (+, -, /, *): ')
    if sign in ('+', '-', '/', '*'):
        if sign == '+':
            print(x+y)
        elif sign == '-0:':
            print(x-y)
        elif sign == '*':
            print(x*y)
        elif sign == '/':
            if y != 0:
                print(x/y)
            else:
                print('Деление на ноль!')
                break
    else:
        print('Неверный знак операции')