# Write your solution here

p1 = input("Password:")
p2 = input("Repeat password:")

while p1 != p2:
    print("They do not match!")
    p2 = input("Repeat password:")
else:
    print("User account created!")