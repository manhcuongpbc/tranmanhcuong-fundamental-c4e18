size = [5,7,300,90,24,50,75]

for i in range(4):
    print("hello, my name is Cuong and there are my sheeps sizes:")
    print(size)
    size = [i+50 for i in size]
    print("\nMONTH", i+1)
    print(i+1, "month passes, now here is my flock:\n", size)
    biggest_size = max(size)
    print("biggest size:{0} let's shear it".format(biggest_size))
    size[size.index(biggest_size)] = 8
    print("after shearing, here is my flock\n", size)

total = sum(size)
print("my flock size in total:", total)
print("I would get:  {0} * {1} $ = {2} $".format(total,2,total*2))