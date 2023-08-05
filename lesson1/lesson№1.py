# 1) Напишите программу, которая спрашивает имя пользователя и затем приветствует его.

num11 = (input('введи имя: '))
print('Привет', num11)

# 2) Напишите программу, которая считывает три числа и выводит их сумму.
# 2.1
print("сумма чисел 50, 20, и 30 равно 100")
# 2.2
num15 = 50
num16 = 20
num17 = 30
num18 = num15 + num16 + num17
print(f' {num15} + {num16} + {num17} = {num18}')
# 2.3
num12 = int(input('Введите первое число: '))
num13 = int(input('Введите второе число: '))
num14 = int(input('Введите третье число: '))
print('Сумма чисел', num12, "," ,num13, "и",  num14,  "равно" , (num12) + (num13) + (num14))

# 3) Напишите программу, для решения следующей задачи: n школьников делят k яблок поровну, неделящийся остаток остается
# в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? Программа получает на
# вход числа n и k и должна вывести искомое количество яблок (два числа).

num19 = 10
num20 = 3
num23 = num19 // num20
num21 = num19 % num20i
print("школьников", num20)
print("яблок", num19)
print("школьникам по", num23, "яблока")
print("остаток в корзине", num21)

# 4) Напишите программу, которая спрашивает число у пользователя и выводит следующее:

num24 = input("введите число: ")
num25 = int(num24) + 1
num26 = int(num24) - 1
print(f"Следующее число для {num24} --> {num25}")
print(f"Предыдущее число для {num24} --> {num26}")

# 5) Напишите программу, которая выводит текст в данном формате

string = """
Twinkle, twinkle, little star,
    How I wonder what you are!
            Up above the world so high
            Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are!"""
print(string)

string = """Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\tUp above the world so high \n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are!"""
print(string)

# 6) Напишите программу для использования метода форматирования следующих трех переменных в соответствии
# с ожидаемым результатом.

totalMoney = 1000
quantity = 3
price = 450
print("у меня ", totalMoney, "долларов" ',' 'поэтому я могу купить', quantity, "футбольных мяча за", price, "долларов")

# 7) Создайте две переменных, со значением ‘spam’ и ‘eggs’, затем распечатайте объединив две переменной в одну целую

num29 = 'spam'
num30 = 'eggs'
print(num29+num30)