my_str = "In phone book: 3 contacts."
# в цикле передаем список (заменяемое, подставляемое) в метод replace
for x, y in ("3", "5"), ("contacts", "names"):
    my_str = my_str.replace(x, y)
print(my_str) # Выведет "In phone book: 5 names."