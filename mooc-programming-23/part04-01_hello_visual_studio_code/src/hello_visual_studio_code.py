# Write your solution here
word = input("Editor:")
word = word.lower()

while word.lower != 'visual studio code':
    if word.lower() in ['notepad', 'word']:
        print('awful')
    elif word.lower() == 'visual studio code':
        print("an excellent choice!")
        break
    else:
        print("not good")
    word = input("Editor:")

