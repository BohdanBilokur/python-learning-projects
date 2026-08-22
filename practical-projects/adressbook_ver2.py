#V2
# Завершение работы программы командой 'ex'
# Вывел показ количества контактов в тел. книге с авто-добавлением/удалением
# Контакты вывел списком сверху
# Добавил команду "all" для показа всех конта ктов в книге
# Добавил авто-копирование всех файлов на компютер после выхода из программы

contacts = ['Artur Artur', 'Igor Igor', 'Liza Liza']
running = True

print('In phone book:', len(contacts), 'contacts.')
while True:
	something = input('Input name:')
	if len(something) < 2:
		print('Too short')

	if something == 'artur':
		print('Artur Artur, number: +44 7000 000001, age: 21')

	else:
		if something == 'igor':
			print('Igor Igor, number: +44 7000 000002, age: 40')

		else:
			if something == 'liza':
				print('Liza Liza, number: +44 7000 000003, age: 12')
			else:
				if something == 'all':
					print('Liza Liza, number: +44 7000 000003, age: 12 \nIgor Igor, number: +44 7000 000002, age: 40 \nArtur Artur, number: +44 7000 000001, age: 21')
				else:
					print('Not found')
		if something =='ex':
			print('Shutting down')
			break
		
import pickle
# Данные контактов
mycontacts = ['Artur Artur, number: +44 7000 000001, age: 21, \nIgor Igor, number: +44 7000 000002, age: 40, \nLiza Liza, number: +44 7000 000003, age: 12']
# Имя файла в котором мы сохраним обьект
contactsfile = 'contacts.data'

# Запись в файл
f = open(contactsfile, 'wb')
pickle.dump(mycontacts, f) # помещаем обьект в файл
f.close()

del mycontacts # уничтожаю переменную mycontacts

# считываем из хранилища
f = open(contactsfile, 'rb')
storedlist=pickle.load(f) # загружаем обьект из файла
print('Copy saved in D:\Python\Practice')