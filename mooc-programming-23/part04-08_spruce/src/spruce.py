# Write your solution here
def spruce(num):
    print("a spruce!")
    j=1
    for i in range(num):
        x = "*"*j
        print(x.center(num*2 -1))
        j+=2
    print("*".center(num*2-1))
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)