for i in range(3):
    for j in range(5):
        print("* ",end='')
    print()

for i in range(5):
    print('*'*i)


for i in range(10):
    print(" "*(10-i) + "*"*i)


print('*'* 10)
for i in range(10):
    print(" "*(10-i)+"*")
print('*'* 10)

for i in range(10):
    for j in range(10):
        if j <= 10 - i - 1:
            print(" ",end ='')
        else:
            print("*",end='')


