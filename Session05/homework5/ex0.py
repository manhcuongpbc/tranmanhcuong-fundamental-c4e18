string = input("Moi nhap string: ")
chars = list(string)
print(chars)
dic = {}
for i in chars:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

for key in dic:
    print("{0} : {1}".format(key, dic[key]))