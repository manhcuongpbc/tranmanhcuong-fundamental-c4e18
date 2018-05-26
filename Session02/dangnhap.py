from getpass import getpass

user_name = input("user name:")
password = getpass("moi nhap pass:")

if user_name != "manhcuong":
    print("ko co user")

elif password != "12345":
    print("wrong password")

else:
    print("dang nhap thanh cong")