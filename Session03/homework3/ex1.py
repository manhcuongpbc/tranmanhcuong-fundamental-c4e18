items = ['T-shirt', 'sweater']
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)?")

    if n == "R":
        print("our items:",end=' ')
        print(*items,sep=', ')

    elif n == "C":
        new_item = input("enter new item: ")
        items.append(new_item)
        print("our items:",end=' ')
        print(*items,sep=', ')

    elif n == "U":
        pos = int(input("update pos: "))
        items[pos-1] = input("new item?")
        print("our items:",end=' ')
        print(*items,sep=', ')

    elif n == 'D':
        pos = int(input("delete pos: "))
        items.remove(items[pos-1])
        print("our items:",end=' ')
        print(*items,sep=', ')
