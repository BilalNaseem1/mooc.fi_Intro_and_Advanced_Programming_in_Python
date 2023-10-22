# Write your solution here
def same_chars(word, a, b):
    try:

        if word[a] == word[b]:
            return True
        else:
            return False
    except IndexError:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 20))