# Write your solution here

def first_word(sentence):
    y = sentence.split()
    return y[0]

def second_word(sentence):
    y = sentence.split()
    return y[1]

def last_word(sentence):
    y = sentence.split()
    return y[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

