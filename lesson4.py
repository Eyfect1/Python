# Задание 1
# Пользователь вводит стороны прямоугольника, выведите его площадь и периметр.
# На вход программе могут подаваться как целые числа, так и вещественные

a = float(input ("первая сторона прямоугольника "))
b = float(input ("вторая сторона прямоугольника "))
S = a * b
P = 2 * a + 2 * b
print("Площадь прямоугольника", S ,"Периметр прямоугольника", P)

# Задание 2
# Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень количества единиц.
# Затем умножит это число на количество сотен. И делит получившееся число на разность количества десятков тысяч и количества тысяч
# Например, есть число 46275
# Необходимо возвести 7 (десятки) в степень 5 (единицы), умножить получившееся число на 2 (сотни),
# и разделить на разность между 4 (десятки тысяч) и 6 (тысячи) то есть (4-6)
# В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0

number = int(input("Введите пятизначное число: "))

tens_of_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

step1 = tens ** units
step2 = step1 * hundreds
step3 = step2 / (tens_of_thousands - thousands)

print(step3)