# Write your solution here

word = input("Please type in a word")
char = input("Please type in a character")

for i in range(0, len(word)-1):
    if word[i] == char:
        if len(word[i:i+3])>=3:
            print(word[i:i+3])
            break
        else:
            break