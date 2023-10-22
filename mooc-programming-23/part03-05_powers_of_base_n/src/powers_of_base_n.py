# Write your solution here

# Write your solution here
upper_limit = int(input("Enter the upper limit: "))
base = int(input("Base:"))

# Initialize a variable to store the current number
number = 1

# Print powers of two until the next number exceeds the upper limit
while number <= upper_limit:
    print(number)
    number *= base