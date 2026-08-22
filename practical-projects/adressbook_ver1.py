#V1

name = 'Artur'   #Использую сamel case переменную
name = 'Igor'
running = True

while True:
	something = input('Input name:')
	if len(something) < 2:
		print('Too short')

	if something == 'Artur':
		print('Artur Artur, number: +44 7000 000001, age: 21')
	else:
		if something == 'Igor':
			print('Igor Igor, number: +44 7000 000002, age: 40')
		else:
			if something == 'Liza':
				print('Liza Liza, number: +44 7000 000003, age: 12')
			else:
				print('Not found')

	if something =='exit':
		break
