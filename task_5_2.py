num = int(input('Введите число!'))
proiz = 1
summ = 0
while num != 0:
    last_digit = num % 10
    summ += last_digit
    proiz *= last_digit
    num = num // 10
print('Сумма цифр равна', summ)
print('Произведение цифр равно', proiz)