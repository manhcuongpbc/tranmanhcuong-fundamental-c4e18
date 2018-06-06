numbers = [1,6,5,7,8,5,6,7,4,5,6,7,4,3,45,6]

n = int(input("Enter a number: "))
count = 0
for i in numbers:
    if i == n:
        count += 1

print("{0} appears {1} times".format(n, count))