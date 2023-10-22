# Write your solution here
st = input("Please type in a string:")
a = 0
e = 0
o = 0

for i in st:
    if i == "a":
        a +=1
    elif i == "e":
        e +=1
    elif i == "o":
        o +=1

if a>0:
    print("a found")
else:
    print("a not found")

if e>0:
    print("e found")
else:
    print("e not found")

if o>0:
    print("o found")
else:
    print("o not found")