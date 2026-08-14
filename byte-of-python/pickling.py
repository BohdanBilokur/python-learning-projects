import pickle

# имя файла, в котором мы сохраним обьект
myproductsfile = 'myproducts.data'
# список покупок
myproducts = ['помидоры, манго, бананы']

# запись в файл
f = open(myproductsfile, 'wb')
pickle.dump(myproducts, f) # помещаем обьект в файл
f.close()

del myproducts # уничтожаю переменную myproducts

# считываем из хранилища
f=open(myproductsfile, 'rb')
storedlist=pickle.load(f) # загружаем обьект из файла
print(storedlist)