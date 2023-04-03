# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Вариант 1

first_comma = my_favorite_songs.find(',') # Индекс первой запятой
# print(first_comma)
last_comma = my_favorite_songs.rfind(',') # Индекс последней запятой
# print(last_comma)
second_comma = my_favorite_songs.find(',',first_comma + 1) # Индекс второй запятой
# print(second_comma)
prelast_comma = my_favorite_songs.rfind(',',0, last_comma-1) # Индекс предпоследней запятой
# print(prelast_comma)
print(my_favorite_songs[:first_comma])
print(my_favorite_songs[last_comma + 2:])
print(my_favorite_songs[first_comma + 2:second_comma])
print(my_favorite_songs[prelast_comma + 2:last_comma])

# Вариант 2

mfs = my_favorite_songs.split(', ') # Конвертируем строку в список
print(mfs[0],mfs[-1],mfs[1],mfs[-2], sep='\n')

# да, вариант 2 это самый топ) добавить нечего)
