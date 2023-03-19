# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
  i_min = arr[0]
  for i in arr:
    if i < i_min:
      i_min = i
  return i_min 

def maximum(arr):
  i_max = arr[0]
  for i in arr:
    if i > i_max:
      i_max = i
  return i_max 
  
list_1 = [4,6,2,1,9,63,-134,566]       
list_2 = [-52, 56, 30, 29, -54, 0, -110]
list_3 = [42, 54, 65, 87, 0]
list_4 = [5]

min_1 = minimum(list_1)
max_1 = maximum(list_1)
print('min =', min_1,', max =', max_1)
min_2 = minimum(list_2)
max_2 = maximum(list_2)
print('min =', min_2,', max =', max_2)
min_3 = minimum(list_3)
max_3 = maximum(list_3)
print('min =', min_3,', max =', max_3)
min_4 = minimum(list_4)
max_4 = maximum(list_4)
print('min =', min_4,', max =', max_4)
