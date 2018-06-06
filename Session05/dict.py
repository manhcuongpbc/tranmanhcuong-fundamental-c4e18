teencode = {
    "vk":"vợ",
    "ck":"chồng",
    "cc":"cục kít =)))",
    "stt":"status"
}

while True:
    for i in teencode:
        print(i,end='\t')
    request = input("\nyour code: ")
    if request in teencode:
        print("*"*20, teencode[request], "*"*20, sep='\n')
    if request not in teencode:
        rq2 = (input("do you want add to ur teencode:y/n ")).lower()
        if rq2 == 'y':
            teencode[request] = input("nghia tuong ung:")
        else:
            break