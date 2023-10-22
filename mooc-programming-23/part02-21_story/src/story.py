sentence = ""
w1 = None
w2 = None
while True:
    w1 = input("Please type in a word")
    if w1 == "end":
        print(sentence)
        break
    elif w1 == w2:
        print(sentence)
        break
    else:
        sentence += w1 + " "
    w2 = input("Please type in a word")
    if w2 == "end":
        print(sentence)
        break
    elif w1 == w2:
        print(sentence)
        break
    else:
        sentence += w2 + " "

