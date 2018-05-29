# food1 = "salad nga"
# food2 = "chocolate"
# food3 = "sò huyết"
# food4 = "mif toom"
# food5 = " phở"
menu = ["mì tôm","b","c","Phở","e"]

#seperator
# print(*menu,sep = ', ')

# menu.append("trung ca")
# print(*menu, sep =', ')
# print(len(menu))

# print(menu[-1])
for i in menu:

    print(i)
# for i in range(len(menu)):
#     # print(i+1 ,". ", menu[i],sep='')
#     print("{0}. {1} ".format(i+1,menu[i]))

for index, item in enumerate(menu):
    print("{0}. {1}".format(index,item))


menu[2] = "cua"
print(menu)