# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.
some_name = 'John'
some_surname = 'Malcovich'
some_age = 39
print(f'Имя объекта {some_name}')
print(f'Фамилия объекта {some_surname}')
print(f'Возраст объекта {some_age} \n')
surname_user = input('Введите вашу фамилию: ')
name_user = input('Введите ваше имя: ')
age_user = input('Введите ваш возраст: ')
print(f'Вас зовут {surname_user} {name_user} и вам {age_user} лет')