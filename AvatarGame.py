#rock-paper-scizors test customised
import random

def avatar_game():
    if computer_choice[0] == user_choice[0]:
        print('TIE \n You must now fight an agni kai!')
    elif user_choice[0] == 'w' and (computer_choice[0] == 'f'or computer_choice[0] == 'a'):
        if computer_choice[0] == 'f':
            print('OF course water beats fire! have you seen the first season?')
        else:
            print('Water 💧 beats air, i mean, she IS his girlfriend. . . :)')
        print('You win!')
    elif user_choice[0] == 'e' and (computer_choice[0] == 'a' or computer_choice[0] == 'w'):
        if computer_choice[0] == 'a':
            print('Earth beats air, after all- she is THE GREATEST EARTH BENDER OF ALL TIME!')
        else:
            print('Although this is close:\n Earth beats water')
        print('You win!')
    elif user_choice[0] == 'f' and (computer_choice[0] == 'b' or computer_choice[0] == 'e'):
        if computer_choice[0] == 'b':
            print('Fire beats boomerang')
        else:
            print('fire 🔥 beats earth, remember him burning her feet?')
        print('You win!')
    elif user_choice[0] == 'a' and (computer_choice[0] == 'f' or computer_choice[0] == 'b'):
        if computer_choice[0] == 'f':
            print('OF course air beats fire! have you seen the first season?')
        else:
            print('air beats boomerang')
        print('You win!')
    elif user_choice[0] == 'b' and (computer_choice[0] == 'e' or computer_choice[0] == 'w'):
        if computer_choice[0] == 'e':
            print('boomerang beats earth, she is blind after all')
        else:
            print('boomerang beats water, older brothers always win ;)')
        print('You win!')
    elif user_choice[0] == "q":
        print('Thanks for playing!')
    else:
        print('You lose :( Computer wins :D \n (try entering you choice again')

    print('The computer choose', computer_choice)

while(True):
    computer_choice = random.choice(['earth', 'water', 'air', 'fire', 'boomerang'])
    user_choice = input('Enter water, earth, fire, air, or boomerang:\n').lower()
    avatar_game()
    if user_choice[0] == 'q':
        break





