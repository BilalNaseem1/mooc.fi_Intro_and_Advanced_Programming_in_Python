# Write your solution here

def even_numbers(lst):
    even_lst = []
    for i in lst:
        if i%2 == 0:
            even_lst.append(i)
        else:
            pass
    return even_lst

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    result = even_numbers(lst)
    print(f"original {lst}")
    print(f"new {result}")
