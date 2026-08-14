#Дебильный калькулятор V2

from colorama import init
init()
from colorama import Fore, Back, Style

print(Fore.BLACK)
print(Back.MAGENTA)

what = input('Что делаем? (+, -, /, *): ')

print(Back.CYAN)

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))

print(Back.GREEN)

if what == '+':
	c = a + b
	print('Результат: ' + str(c))

elif what == '-':
	c = a - b
	print('Результат: ' + str(c))

elif what == '/':
	c = a / b
	print('Результат: ' + str(c))

elif what == '*':
	c = a * b
	print('Результат: ' + str(c))

else:
	print('Неверная операция!')

input()
