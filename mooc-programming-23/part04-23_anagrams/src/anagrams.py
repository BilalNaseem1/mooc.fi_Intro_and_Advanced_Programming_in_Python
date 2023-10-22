# Write your solution here

def anagrams(w1, w2):
    w1n = sorted(w1)
    w2n = sorted(w2)

    if w1n ==w2n:
        return True
    else:
        return False
    
if __name__ =="__main__":
    result = anagrams("tabby", "batty")
    print(result)