name = 'Bohdan' #Это обьект строки

if name.startswith('Bo'):
	print('Да, строка начинается на "Bo"')

if 'h' in name:
	print('Да, она содержит строку "h"')

if name.find("ohd") != -1:
	print('Да, она содержит строку "ohd"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))