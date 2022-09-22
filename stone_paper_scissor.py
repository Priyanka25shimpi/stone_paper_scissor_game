import random

# Stone Paper Scissor Game
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose stone
    elif comp == 'stone':
        if you=='paper':
            return True
        elif you=='scissor':
            return False
    
    # Check for all possibilities when computer chose paper
    elif comp == 'paper':
        if you=='stone':
            return False
        elif you=='scissor':
            return True
    
    # Check for all possibilities when computer chose scissor
    elif comp == 'scissor':
        if you=='paper':
            return False
        elif you=='stone':
            return True

print("Comp Turn: Stone, paper or scissor?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'stone'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

you = input("Your Turn: Stone, paper or sscissor?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")