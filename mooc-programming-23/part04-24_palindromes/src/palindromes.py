# Write your solution here


def palindromes(word):

    y = word[::-1]

    if word ==y:
        return True
    else:
        return False

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word) is True:
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
            



# # Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
#     while True:
#         word = input("Please type in a palindrome: ")
#         if palindromes(word) is True:
#             print(f"{word} is a palindrome")
#             break
#         else:
#             print("that wasn't a palindrome")
            


    
