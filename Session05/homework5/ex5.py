prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear' : 15
}

for key in prices.keys():
    print(key)
    print("price: ", prices[key])
    print("stock: ", stock[key])
    print()

total = 0
for key in prices:
    pr = prices[key] * stock[key]
    print("gia cua {0} la {1}".format(key, pr))
    total += pr
print(total)