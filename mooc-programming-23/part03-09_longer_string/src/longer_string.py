# Write your solution here
st1 = input("Please type in string 1:")
st2 = input("Please type in string 2:")

s1 = 0
s2 = 0

for i in st1:
    s1 +=1
for i in st2:
    s2 +=1

if s1 > s2:
    print(f"{st1} is longer")
elif s1 < s2:
    print(f"{st2} is longer")
else:
    print("The strings are equally long")