bacteria = int(input("How many B bacterias are there? "))
minutes = int(input("how much time? "))

bacs = bacteria * (2 ** (minutes//2))

print("after {0} minutes, we would have {1} bacs".format(minutes, bacs))