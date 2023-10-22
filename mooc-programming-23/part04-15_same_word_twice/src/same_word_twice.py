# Write your solution here

lst = []

while True:

    w = input("Word: ")

    if w in lst:
        break
    else:
        lst.append(w)

print(f"You typed in {len(lst)} different words")