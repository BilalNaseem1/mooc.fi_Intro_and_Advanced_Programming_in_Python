# Write your solution here

st = input("Please type in a string:")
length = len(st)
i = 0
while i <= len(st):
    i +=1
    print(st[-i])
    if abs(i) >= len(st):
        break
