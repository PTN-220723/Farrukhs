# num1 = '12'
# print(int(num1))
# print(type(num1))

# input('sssss')
# temp = input('sssss  ')
# print(type(temp))

# a1 = int(temp) + 1
# a2 = int(temp) - 1

# temp = int(input('sssss'))
# a1 = int(temp) + 1
# print(a1)

# a = 12
# b = 2
# c = a
# a = b
# b = c
# print('a' , a )
# print('b', b)

# a = 12
# b = 2
# temp1 = a
# temp2 = b
# a = temp2
# b = temp1
# print('a', a)
# print('b', b)

# q1, q2 = 12, 34
# print(q1)
# print(q2)

# a = 12
# b = 2
# temp1 = a
# temp2 = b
# a = temp2
# b = temp1
# a, b = temp2, temp1
# print('a', a)
# print('b', b)

# a = 12
# b = 3
# a, b = b, a
# print('a', a)
# print('b', b)

# a = 0
# b = 0
# c = 0

# a = b = c = 0
# print(a+1)
# print(b+2)
# print(c+3)
# print(a)

# a = 0
# print(id(a))
# a = a +1
# print(id(a))

# срезы строк

# stping = "язык"
# print(stping[0])
# print(stping[1])
# print(stping[2])
# print(stping[3])

# stping = "язык програмирование пайтон"
# print(stping[3:])
# print(stping[2:8])
# # [] не включительно
# # () включительно
# print(stping[2:8:2])

# string = 'програмирование'
# print(string[0:16:1])
# print(string[0:16:2])
# print(string[0:16:3])

# string = 'программирование'
# print(string[15])
# print(string[-1])
# print(string[-16])

# string = 'программирование'
# print(string[::-1])
# print(string[0:16:-1])
# print(string[::-1])
# print(string[::0])

# string = 'I love Python'
# print(string.lower()) все самые маленькие
# print(string.upper()) все большие
# print(string.capitalize()) заглавную
# print(string.title()) каждая первая большая

# string = 'I love Python'
# a = string.upper()
# print(a)

# string = 'I love Python'
# result = string.isupper()
# print(result)
# print(type(result))
#
# string = 'I love Python'
# result = string.isdigit()
# print(result)
# print(type(result))
#
# string = 'I love Python'
# result = string.isascii()
# print(result)
# print(type(result))
#
# string = '12'
# result = string.isupper()
# print(result)
# print(type(result))
#
# string = 'I love Python'
# result = string.startswith('i')
# print(result)
# print(type(result))

# Abc = 12
# abc = 23
# print(Abc)
# print(abc) bool это не строка

# string = 'I love Python'
# result = string.lower().startswith('i')
# print(type(result))

# string = 'I love Python'
# result = string.lower().upper().title().capitalize()
# print(type(result))
# print(result)

# string1 = 'i love python'
# string2 = string1.replace('python', 'Linux')
# print(string2)
# print(string2.endswith('linux'))

# string = 'I love Python'
# print(string.count('o'))
# print(string.count('i'))
# print(string.count('I'))
# print(string.find('love'))
# print(string.find('Love'))

# string = '      I love Python   -    '
# string1 = '!!!!'
# print(string, string1, sep='')
# string = string.strip()

# string = '  +    I love Python   -    '
# print(string.strip().rstrip('-').rstrip())
# print(string.strip().rstrip('-').lstrip('+').strip())
# print(string.rstrip('-').lstrip('+').strip())

# string = '  +    I love Python   -    '
# string = string.replace('+','').replace('-','').strip()
# print(string)

# string1 = 'I love Python'
# string2 = string1.split()
# print(string2)

# string1 = 'I:love:Python'
# string2 = string1.split(':')
# print(string2)
# string3 = ' '.join(string2)
# print(string3)
# string1.translate(string3)
# print(string1)
# print(string2)
# print(string3)


INPUT_FOR_SITS_NUMBER = input('введите номер вашего места: ')
DIVISION_OF_SITS = (int(INPUT_FOR_SITS_NUMBER) - 1) // 4 + 1

print(f'(номер вашего купе: {DIVISION_OF_SITS})')