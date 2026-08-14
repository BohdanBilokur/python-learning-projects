print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist #Присвоил еще одно имя

del shoplist[0] #Первая покупка сделана, поэтому удаляем ее

print('shoplist:', shoplist)
print('mylist:', mylist)

print('Копирование при помощи полной вырезки')
print('mylist:', mylist)
#Обратите внимание, что теперь списки разные