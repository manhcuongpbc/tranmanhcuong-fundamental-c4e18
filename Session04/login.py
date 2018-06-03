count = 0
while True:
    if count == 3:
        print("fail 3 times")
        break
    else:
        name = input("user name: ")
        if name == 'c4e':
            passs = input("pass: ")
            if passs == 'aaa':
                print("login success")
                break
            else:
                print("pass is incorrect")
        else:
            if count <= 2:
                print("nhap lai username")
    count += 1