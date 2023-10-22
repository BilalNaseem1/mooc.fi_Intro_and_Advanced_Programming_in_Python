# Write your solution here

ls = []

print("The list is now []")

opt = input("a(d)d, (r)emove or e(x)it:")
i = 1

while opt != "x":
    if opt =="d":
        ls.append(i)
        i +=1
    elif opt == "r":
        ls.pop(-1)
    print(f"The list is now {ls}")
    opt = input("a(d)d, (r)emove or e(x)it:")
    if len(ls) ==0:
        i =1
    else:
        i = ls[-1] +1
print("Bye!")