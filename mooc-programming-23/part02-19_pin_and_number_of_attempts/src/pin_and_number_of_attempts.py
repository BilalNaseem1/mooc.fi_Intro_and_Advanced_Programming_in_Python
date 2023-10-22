# Write your solution here

pin = int(input("PIN: "))
count = 1

while pin != 4321:
    print("Wrong")
    count += 1
    pin = int(input("PIN: "))
else:
    if count == 1:
        print("Correct! It only took you one single attempt!")
    else:
        print(f"Correct! It took you {count} attempts")
