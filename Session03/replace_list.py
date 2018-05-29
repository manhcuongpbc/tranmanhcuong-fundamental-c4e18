favorite = ["an com ne","danh dan", "hoc bai"]
for idex,item in enumerate(favorite):
    print("{0}. {1}".format(idex+1, item))
i = int(input("vi tri muon sua:"))
new_favorite = input("cai muon sua: ")
favorite[i-1] = new_favorite
for idex,item in enumerate(favorite):
    print("{0}. {1}".format(idex+1, item))
