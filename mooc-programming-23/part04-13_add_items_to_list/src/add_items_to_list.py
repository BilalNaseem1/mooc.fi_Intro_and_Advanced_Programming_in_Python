# Write your solution here

num = int(input("How many items:"))

ls = []

for i in range(1, num+1):
    x = int(input(f"Item {i}:"))
    ls.append(x)
    i+=1

print(ls)
