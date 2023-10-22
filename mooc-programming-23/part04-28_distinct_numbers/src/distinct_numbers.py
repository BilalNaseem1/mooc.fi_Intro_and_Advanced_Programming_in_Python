# Write your solution here

def distinct_numbers(lst):
    unique_list = []
    for i in lst:
        if i in unique_list:
            pass
        else:
            unique_list.append(i)
    return sorted(unique_list)