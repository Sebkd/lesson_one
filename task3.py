#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
#Считаем 3 + 33 + 333 = 369.
while True:
    new_number = int(input('Введите целое число n от 0 до 9: '))
    if (new_number > 0 and new_number < 10):
        break
    else:
        print('Вы ввели или меньше 0 или больше 9, попробуйте еще раз')

new_number = new_number + int(str(str(new_number)+str(new_number))) + int(str(str(new_number) + str(new_number) + str(new_number)))
print(f'Сумма вашего числа в формате n+nn+nnn {new_number}')