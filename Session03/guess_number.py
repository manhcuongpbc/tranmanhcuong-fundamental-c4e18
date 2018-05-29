from random import randint
n = randint(0,100)
print(n)
loop = True
count = 0
while loop:
    guess_n = int(input("guess: "))
    if count == 7:
        loop = False
        print("lose")
    else:
        if guess_n > n:
            print("too large")
        elif guess_n < n:
            print("too small")
        else:
            print("bingo")
            loop = False
    count += 1
        
