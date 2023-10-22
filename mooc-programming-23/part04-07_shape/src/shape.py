# Copy here code of line function from previous exercise and use it in your solution
def line(num, word):
    if word == "":
        print("*" * num)
    else:
        print(word[0] * num)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size+1):
        line(i, "#")

def shape(k, a, l, b):
    for i in range(k+1):
        line(i, a)
    for j in range(l):
        line(k, b)
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")