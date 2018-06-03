n = int(input("moi nhap so: "))
if n == 2 or n == 3:
    print("la snt")
elif n < 2:
    print("ko la snt")
else:
    is_prime = True
    k = int(n**0.5)
    for i in range(2,k+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("la snt")
    else:
        print("0")
