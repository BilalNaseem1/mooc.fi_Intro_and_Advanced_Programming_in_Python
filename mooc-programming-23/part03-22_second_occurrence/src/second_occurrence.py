# Input from the user
user_string = input("Please type in a string: ")
user_substring = input("Please type in a substring: ")

# Find the index of the first occurrence of the substring
first_occurrence = user_string.find(user_substring)

if first_occurrence == -1:
    print("The substring does not occur twice in the string.")
else:
    # Find the index of the second occurrence, starting after the first occurrence
    second_occurrence = user_string.find(user_substring, first_occurrence + len(user_substring))
    
    if second_occurrence == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_occurrence}.")
