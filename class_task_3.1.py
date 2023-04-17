# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

class Matrix(object):
 
    def __init__(self, rows, cols):
        self.field = [[1 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
 
    def get_val(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return
 
    def get_row(self, row):
        return self.field[row]

    def set_val(self, row, col, val):
        self.field[row][col] = val
 
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols
 
    def add_row(self, row):
        self.field.insert(row, [1] * self.cols)
        self.rows += 1
 
    def add_col(self, col):
        for row in range(self.rows):
            self.field[row].insert(col, 1)
        self.cols += 1
 
    def del_row(self, row):
        self.field.pop(row)
        self.rows -= 1
 
    def del_col(self, col):
        for row in range(self.rows):
            self.field[row].pop(col)
        self.cols -= 1

# Функция вывода экземпляра класса
def prin_t(m_x):
    for i in range(m_x.n_rows()):
        print(m_x.get_row(i))
    return

# Экземпляр класса
m = Matrix(10, 10)
print('Печать экземпляра класса')
prin_t(m)

# Число строк и столбцов
print('Число строк и столбцов матрицы')
print(m.n_rows(), 'x', m.n_cols())

# Установить значания элементов матрицы
m.set_val(3, 5, 6)
m.set_val(7, 8, 4)
m.set_val(6, 3, 9)
print('Изменение значений элементов матрицы')
prin_t(m)

# Добавить столбец
m.add_col(4)
print('Добавление столбца в матрицу')
prin_t(m)

# Удалить столбец
m.del_col(4)
print('Удаление столбца')
prin_t(m)

# Добавить строку
m.add_row(2)
print('Добавление строки')
prin_t(m)

# Удалить строку
m.del_row(2)
print('Удаление строки')
prin_t(m)