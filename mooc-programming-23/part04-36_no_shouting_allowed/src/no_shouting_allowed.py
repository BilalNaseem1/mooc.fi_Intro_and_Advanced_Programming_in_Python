# Write your solution here
def str_in_list(string):
    x = 0
    for i in string:
        if i.isupper() == True:
            x+=1
    return True if x == len(string) else False

def no_shouting(lst):
    new_list = []
    for st in lst:
        j = str_in_list(st)
        if j != True:
            new_list.append(st)
    return new_list

if __name__ == "__main__":
    k = no_shouting(['FIRST', 'second', 'THIRD', 'fourth'])
    print(k)
