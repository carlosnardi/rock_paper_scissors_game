import random

user = ''

def define_item(number):
  if number == 0:
    print('Rock')
  elif number == 1:
    print('Paper')
  elif number == 2:
    print('Scissor')


while user != 3:
  computer_list = [0, 1, 2]
  computer = random.choice(computer_list)
  user = int(input('Type 0 for rock, 1 for paper, 2 for scissor or 3 for exit: '))
  user_choice = define_item(user)
  computer_choice = define_item(computer)

  if user == computer:
    print('Draw')
  elif user == 0 and computer == 1:
    print('Lose')
  elif user == 0 and computer == 2:
    print('Win')
  elif user == 1 and computer == 0:
    print('Win')
  elif user == 1 and computer == 2:
    print('Lose')
  elif user == 2 and computer == 0:
    print('Lose')
  elif user == 2 and computer == 1:
    print('Win')
  
print('Thanks for playing')
    

  
