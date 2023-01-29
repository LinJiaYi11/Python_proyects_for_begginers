from random import randint

#Logo
logo = '''  
  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       '''

#Function to check if the guess is correct
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns-1
  elif answer > guess:
    print("Too low.")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}!")

#Function to define difficulty level
easy_level = 10
hard_level = 5

def set_diff():
  diff = input("Choose a difficulty. Type 'easy' or 'hard': " ) 
  if diff == "easy":
    return easy_level
  elif diff == "hard":
    return hard_level

def game():
  #Welcoming  
  print("Welcome to the Number Guessing Game!\nThink of a number between 1 and 100.")

  #Define the answer
  answer = randint(1,100)

  #Call set difficulty level and get number of turns
  turns = set_diff()
  

  #Take inputs and check answer
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    #check anwer and obtain turns
    turns = check_answer(guess, answer, turns)
    
    if turns == 0:
      print(f"You have run out of turns. You lose.")
      return
    elif guess != answer:
      print("Guess again.")

#Main
print(logo)
game()




