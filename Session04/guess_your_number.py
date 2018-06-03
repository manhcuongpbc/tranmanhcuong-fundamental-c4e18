low = 0
high = 100
mid = 50
print('''
c nếu đúng
l nếu lớn hơn số mày nghĩ
s nếu nhỏ hơn số mày nghĩ
''')
while True:
    ans = input("is {0} ur number ".format(mid)).lower()
    if ans == 's':
        low = mid
    elif ans == 'l':
        high = mid
    elif ans == 'c':
        print("tao giỏi vl")
        break
    mid = (low+high)//2
    if low == high:
        print("đcmm chơi bố à ? đmm")
        break