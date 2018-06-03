money = input("moi nhap so tien ban co: ")
s1 = list(money)
s2 = [int(i) for i in s1]

print(s2)
for i in range(len(s2)):
    if s2[i] != 0:
        # print(i)
        break
for j in range(i):
    s2.pop(0)
print(s2)

# block = len(s2) // 3
# thua = len(s2) % 3
# print(s2[0:thua])
# for i in range(block):
#     print(*(s2[thua * i : thua * i + 3]), end=',')

