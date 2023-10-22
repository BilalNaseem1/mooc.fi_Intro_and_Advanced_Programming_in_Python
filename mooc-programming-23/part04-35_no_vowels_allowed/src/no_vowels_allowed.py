# Write your solution here

def no_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str1 = ""
    for i in string:
        if i in vowels:
            pass
        else:
            str1 +=i
    return str1

if __name__ == "__main__":
    k = no_vowels("abcaa")
    print(k)