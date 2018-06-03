n = input("sequence of numbers: ")
k = n.strip().split()
print(k)
diem =[int(i) for i in k]

if diem == sorted(diem):
    print("da sap xep")
else:
    print("chua sap xep")

for i in range(len(diem)-1):
    if diem[i] <= diem[i+1]:
        is_sorted = True
    else:
        is_sorted = False
        break
if is_sorted:
    print("da sap xep")
else:
    print("chua sap xep")
    sort = []
    k = sorted(diem,reverse = True)
    print(k)
    for i in range(len(diem)):
        min_ = min(diem)
        sort.append(min_)
        diem.pop(diem.index(min_))
    print("after sort ",(*sort))