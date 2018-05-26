for i in range(9):
    for j in range(9):
        if (j%2 and i%2) or (j%2==0 and i%2==0):
            print("1",end=' ')
        else:
            print("0",end=' ')
    print()

n = int(input("moi nhap n: "))

for i in range(n+1):
    for j in range(n+1):
        if (j%2 and i%2) or (j%2==0 and i%2==0):
            print("1",end=' ')
        else:
            print("0",end=' ')
    print()