n = input("moi nhap list cac phan tu: ")
new_list = [int(i) for i in n.split(" ")]
print((new_list))
for i in range(len(new_list)-1,-1,-1):
    print(i)
    for j in range(1,i+1):
        if new_list[j-1] > new_list[j]:
            swap = new_list[j]
            new_list[j] = new_list[j-1]
            new_list[j-1] = swap
print(new_list)
