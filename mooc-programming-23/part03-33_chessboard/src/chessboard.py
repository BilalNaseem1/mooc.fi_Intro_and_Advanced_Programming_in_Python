# Write your solution here
def chessboard(n):
    row = 1

    while row <= n:
        if row%2 == 0:
            for i in range(n):
                if i%2==0:
                    print(0, end="")
                else:
                    print(1, end="")
        else:
            for i in range(n):
                if i%2==0:
                    print(1, end="")
                else:
                    print(0, end="")
        row+=1
        print()

# Testing the function
if __name__ == "__main__":
    chessboard(3)
