import random
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
cpu = [rock, paper, scissors]

mychoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(cpu[mychoice])

cpu_plays = random.randint(0, 2)
print("Computer chose:")
print(cpu[cpu_plays])

if cpu_plays == mychoice:
    print("It`s a draw, good luck next time.")
elif mychoice == 0 and cpu_plays == 2:
    print("Nice, you won.")
elif mychoice == 1 and cpu_plays == 0:
    print("Nice, you won.")
elif mychoice == 2 and cpu_plays == 1:
    print("Nice, you won.")
elif mychoice == 0 and cpu_plays == 1:
    print("You lose.")
elif mychoice == 1 and cpu_plays == 2:
    print("You lose.")
elif mychoice == 2 and cpu_plays == 0:
    print("You lose.")
