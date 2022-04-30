import random

num=random.randint(1,9)

print('Guess a number between 0 an 10')

chance=0
while chance<5 :
    guess=int(input('Enter your guess: '))
    if guess==num :
        print('Your guess was right! Congratulations!')
        break
    elif guess<num :
        print('Guess a higher number')
    else :
        print('Guess a lower number')
    chance+=1

if chance>=5 :
    print('You lose. The number was', num)