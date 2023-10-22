# Write your solution here
one = input("1st letter:")
two = input("2nd letter:")
three = input("3rd letter:")

if (one < two and two < three) or (three < two and two < one):
    print(f"The letter in the middle is {two}")
elif (two < one and one < three) or (three < one and one < two):
    print(f"The letter in the middle is {one}")
elif (two < three and three < one) or (one < three and three < two):
    print(f"The letter in the middle is {three}")