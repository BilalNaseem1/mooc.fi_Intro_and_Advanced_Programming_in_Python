# Write your solution here

marks = int(input("How many points [0-100]:"))

if marks in range(90, 101):
    print("Grade: 5")
elif marks in range(80, 90):
    print("Grade: 4")
elif marks in range(70, 80):
    print("Grade: 3")
elif marks in range(60, 70):
    print("Grade: 2")
elif marks in range(50, 60):
    print("Grade: 1")
elif marks in range(0, 50):
    print("Grade: fail")
else:
    print("Grade: impossible!")