number = 40
number2 = 100
number0 = 0
guess = int(input('Введите целое число :'))

if guess == number:
	print('Поздравляю вы угадали')
	print('(хотя и не выиграли никакого приза!)')

if guess == number0:
	print('Ответ на много больше')

if guess >= number2:
	print('Ухх ты и загнул, возьми поменьше!')

if 0 < guess < 40:
	print('Нет, загаданное число немного больше');

elif guess >number <number2:
	print('Нет, загаданное число немного меньше за ваше')

print ('Завершено')
