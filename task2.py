# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
data_time = int(input('Введите время в секундах: '))
if (data_time // 3600):
    hour_time = data_time // 3600
    minutes_time = (data_time - 3600 * hour_time) // 60
    data_time = (data_time - 3600 * hour_time - 60 * minutes_time)
elif (data_time // 60):
    hour_time = 0
    minutes_time = data_time // 60
    data_time = (data_time - 60 * minutes_time)
else:
    hour_time = 0
    minutes_time = 0
if (hour_time < 10):
    hour_time = str('0' + str(hour_time))
if (minutes_time < 10):
    minutes_time = str('0' + str(minutes_time))
if (data_time < 10):
    data_time = str('0' + str(data_time))
print(f'Время в формате ЧЧ:ММ:СС {hour_time}:{minutes_time}:{data_time}')
