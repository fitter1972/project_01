# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
random_songs_A = random.sample(my_favorite_songs,3)
print("Пункт А: Три песни звучат", round(random_songs_A [0][1] + random_songs_A [1][1] + random_songs_A[2][1]), "минут")

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

random_songs_B = random.sample(list(my_favorite_songs_dict.items()), 3)
print("Пункт B: Три песни звучат", round(random_songs_B [0][1] + random_songs_B [1][1] + random_songs_B[2][1]), "минут")

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
print('Пункт С-А: ', random_songs_A [0][0],'; ', random_songs_A [1][0],'; ', random_songs_A[2][0], sep = '')
print('Пункт С-B: ', random_songs_B [0][0],'; ', random_songs_B [1][0],'; ', random_songs_B[2][0], sep = '')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
print('Пункт D:')
for i in my_favorite_songs:
    t = str(round(i[1] * 100))
    sec = int(t[-2:])
    min = int(t[:-2])
    t = datetime.time(00,min,sec).strftime('%M:%S')
    i[1] = t
    print(i)
random_songs_D = random.sample(my_favorite_songs,3)
time_sum = datetime.timedelta()
for i in random_songs_D:
    (m, s) = i[1].split(':')
    d = datetime.timedelta(minutes=int(m), seconds=int(s))
    time_sum += d
print("Пункт D: Три песни звучат", time_sum, "минут")

# Интересно) у меня был такой вариант тоже с timedelta
from datetime import timedelta
from math import modf
from random import sample


total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
