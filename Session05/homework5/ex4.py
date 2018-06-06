pairs = [1,1]
month = 2
while True:
    if month <= 15:
        month += 1
        next_month = pairs[-1] + pairs[-2]
        pairs.append(next_month)
        print("month {0}: {1} pairs of rabbit".format(month, pairs[-1]))
    else: 
        break