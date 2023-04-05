# Создание и наполнение таблицы
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()

query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL, 
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query)

query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');
"""
cursor.execute(query)

connection.commit()
connection.close()