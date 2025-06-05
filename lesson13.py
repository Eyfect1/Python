# Задание 1
# С помощью цикла создайте матрицу вида 10x10
# И ещё одну - такой же размерности.
# Итого должно получиться сперва две матрица одинаковой размерности
# И теперь нужно сложить эти две матрицы в третью
# Чтобы заполнить матрицы различными значениями - воспользуйтесь модулем random

import random

matrix1 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(0, 100))
    matrix1.append(row)

matrix2 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(0, 100))
    matrix2.append(row)

matrix3 = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)

print("Первая матрица:")
for row in matrix1:
    print(row)

print("\nВторая матрица:")
for row in matrix2:
    print(row)

print("\nСумма матриц:")
for row in matrix3:
    print(row)