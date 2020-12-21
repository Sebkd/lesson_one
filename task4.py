#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.
while True:
    user_number = input('Введите положительное целое число, больше 10: ')
    if (int(user_number) < 10):
        print('Вы ввели не такое число, которое просили, попробуйте еще раз \n')
        continue
    break
count = 0
max_number = int(user_number[count])
while (len(user_number)-count):
    if (int(user_number[count]) > max_number):
        max_number = int(user_number[count])
    count +=1
print(f'максимальная цифра {max_number}')

