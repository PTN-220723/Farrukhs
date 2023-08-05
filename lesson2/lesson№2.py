# 1) Составить три формы присвоение следующего вида x, y, z = y, z, x (придумать способ применения )

a = 'x'
b = 'y'
c = 'z'
a = 'y'
b = 'z'
c = 'x'
print(c, b, a)
print(a, b, c)

a = 'x'
b = 'y'
c = 'z'
a, b, c = b, c, a
print(c, b, a, '=', a, b, c)

# 2) Распечатать: сложение, вычитание, умножение, деление, возведение в степень следующих переменных:

num1 = '3.14'
num2 = '4'
a = 3.14 + 4
b = 3.14 - 4
c = 3.14 * 4
d = 3.14 / 4
e = 3.14 ** 4
print(f'{num1} + {num2} = {a}')
print(f'{num1} - {num2} = {b}')
print(f'{num1} * {num2} = {c}')
print(f'{num1} / {num2} = {d}')
print(f'{num1}  {num2} = {e}')

# 3) Воспользуйтесь различными методами строк

str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '
print(str1.strip().lstrip('<').lstrip().rstrip('-').rstrip().lower())
print(str2.strip().upper().rstrip().rstrip('\n').rstrip('.').rstrip())
print(str3.strip().lstrip('(').lstrip().rstrip('+').rstrip(':').rstrip().rstrip('-').capitalize())

# 4) Обработайте каждую переменную и получите результат как на картинке:

string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'
print(string1[::-1])
print(string2[6:8],string2[14:20])
print(string3[0:11:2])

# 5) С помощью метода строк Замените слово show на display и создайте другую переменную

show = 'show ip interface brief'
show = show.replace('show', 'display')
print(show)

# 6) ** В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу,
# которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная,
# начинается с 1).

# vokzal = int(input('Введите номер места, а я отвечу в каком купе он нахотится: '))
# box = 36
# room = int(box/vokzal)
# print(f'Место под номером {vokzal} находится в {room} купе')

vokzal = input('Введите номер места, а я отвечу в каком купе он нахотится: ')
room = (int(vokzal) - 1) // 4 + 1
print(f'Место под номером {vokzal} находится в {room} купе')

# 7) Подсчитайте общее количество цифр в числе.
# Например, число 75869 , поэтому на выходе должно быть 5 .

a = 75869
b = str(a)
print(len(b))