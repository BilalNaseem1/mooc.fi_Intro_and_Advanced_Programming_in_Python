# Write your solution here
upper_limit = int(input("Enter the upper limit: "))

# Initialize a variable to store the current number
number = 1

# Print powers of two until the next number exceeds the upper limit
while number <= upper_limit:
    print(number)
    number *= 2