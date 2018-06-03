n = int(input("moi nhap so: "))
if n == 2 or n == 3:
    print("la snt")
elif n < 2:
    print("ko la snt")
else:
    k = int(n**0.5)
    for i in range(2,k+1):
        if n % i == 0:
            is_prime = 1
            print(i)
            break
        else:
            is_prime = 0

    if is_prime == 0:
        print("la snt")
    else:
        print("ko la snt")