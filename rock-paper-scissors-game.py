rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______) 
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to ROCK, Paper, SCISSORS GAME!!!")
user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

if user_choose == 0:
   print(rock)
  
elif user_choose == 1:S
    print(paper)
elif user_choose == 2:
  print(scissors)
else:
    print("Error")

rps = random.randint(0, 3)

if rps == 0:
  print(rock)
elif rps == 1:
  print(paper)
elif rps == 2:
  print(scissors)
  

rule = [[0,0] , [0,1] , [0,2] , [1,0] , [1,1] , [1,2] , [2,0] , [2,1] , [2,2]]
outcome = ['Draw' , 'Cpu wins' , 'You win' , 'You Win' , 'Draw' , 'Cpu Wins' , 'Cpu Win' , 'You Win' , 'Draw']

for i in range(9):
  
  if [user_choose , rps ] == rule[i]:
   print(outcome[i])

