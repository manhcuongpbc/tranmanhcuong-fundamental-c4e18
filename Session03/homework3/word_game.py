from random import choice
word_list = ["champion", "hollyshit","handjob","techkid"]
word = choice(word_list)
chars = list(word)
# print(*chars)
for i in range(len(chars)):
    n = choice(chars)
    print(n,end=' ')
    chars.remove(n)


while True:
    guess_word = input("\nyour answer: ")
    if guess_word == word:
        print("Hura, ăn may vkl")
        break
    else:
        print("ngu vl, doan lai di")