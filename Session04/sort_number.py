l = [10,2,2,-5,4,18]
sort = []
k = sorted(l,reverse = True)
print(k)
for i in range(len(l)):
    min_ = min(l)
    sort.append(min_)
    l.pop(l.index(min_))
print(sort)