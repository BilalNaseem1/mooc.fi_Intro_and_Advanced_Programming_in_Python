# Write your solution here# Write your solution here

num = int(input("Please type in a number:"))
x = 1
k = 1

while num >0:
    while k <= num:
        x *= k
        k +=1
    print(f"The factorial of the number {num} is {x}")
    num = int(input("Please type in a number:"))
    x = 1
    k = 1
else:
    print("Thanks and bye!")


