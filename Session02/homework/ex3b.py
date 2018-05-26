for i in range(10):
    print("1 0",end=' ')

n = int(input("moi nhap n: "))
for i in range(n):
    if i % 2 == 0:
        print("1", end=' ')
    else:
        print("0",end =' ')