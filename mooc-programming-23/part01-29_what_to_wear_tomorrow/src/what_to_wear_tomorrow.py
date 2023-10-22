# Write your solution here
print('What is the weather forecast for tomorrow?')
temp = int(input('Temperature:'))
rain = input('Will it rain (yes/no):')

if rain == 'no':
    if temp>20:
        print('Wear jeans and a T-shirt')
    elif temp>10:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well')
    elif temp>5:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you')
    elif temp>0:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order')
elif rain == 'yes':
    if temp>20:
        print('Wear jeans and a T-shirt')
        print('Don\'t forget your umbrella!')
    elif temp>10:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well')
        print('Don\'t forget your umbrella!')
    elif temp>5:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you')
        print('Don\'t forget your umbrella!')
    elif temp>0:
        print('Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order')
        print('Don\'t forget your umbrella!')