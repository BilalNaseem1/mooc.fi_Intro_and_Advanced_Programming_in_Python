# Write your solution here
# Write your solution here
def squared(word, n):
    rs = ""
    for i in range(0, n**2):
        print(word[i%len(word)], end ="")
        rs += word[i%len(word)]
        if len(rs) % n == 0:
            print()
        if i == n**2:
            break

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)
