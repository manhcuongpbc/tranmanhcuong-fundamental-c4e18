name = input("Moi nhap ten: ")
name_1 = name.strip().lower()
name_2 = name_1.split()
k = [i.title() for i in name_2]
name_3 = ' '.join(k)
print("your name is {0}".format(name_3))