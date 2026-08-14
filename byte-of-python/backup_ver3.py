import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\Program Files\Zeal"']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'D:\Python\Backup_tests' # Подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
#4 Текущая дата служит именем подкаталога (Папки) в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
#Именем для zip-архива служит текущее время.
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла.
comment = input('Введите комментарий -->')
if len(comment) == 0: 'Проверяем введен ли комментарий'
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' +
	comment.replace('', '_') + '.zip'

# Создаем каталог, если его еще нет
if not os.path.exists(today):
	os.mkdir(today) #Создание каталога 
print('Каталог успешно создан', today)

# Имя Zip-файла
target = today + os.sep + now + ".zip"

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
	print('Резервная копия успешно создана в', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')