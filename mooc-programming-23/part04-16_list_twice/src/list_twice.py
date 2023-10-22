# Write your solution here
lst = []
while True:
    i = int(input("New item: "))
    if i ==0:
        break
    lst.append(i)
    print(f"The list now: {lst}")
    print(f"The list in order: {sorted(lst)}")

print("Bye!")