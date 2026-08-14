#V1

name = 'Artur'   #Использую сamel case переменную
name = 'Igor'
running = True

while True:
	something = input('Input name:')
	if len(something) < 2:
		print('Too short')

	if something == 'Artur':
		print('Artur Bilokur, number: 0000000, age: 21')
	else:
		if something == 'Igor':
			print('Igor Bilokur, number: 0000000, age: 40')
		else:
			if something == 'Liza':
				print('Liza Bilokur, number: 0000000, age: 12')
			else:
				print('Not found')

	if something =='exit':
		break
