from turtle import *


so_canh = int(input("moi nhap so canh"))
goc = 180 - ((so_canh -2) * 180 / so_canh)
# print(goc)

shape("turtle")
color("blue")
speed(-1)

for i in range(so_canh):
    forward(50)
    left(goc)
mainloop() 