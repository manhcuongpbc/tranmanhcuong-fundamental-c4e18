import datetime
now = datetime.datetime.now()
print(now)
namsinh = int(input("ban sinh nam may?\n"))
tuoi = now.year - namsinh
print("nam nay ban", tuoi, "tuoi")