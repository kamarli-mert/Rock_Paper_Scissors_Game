import random

print("Welcome to Rock, Paper, Scissors!\n*********************************\n'R' for Rock, 'P' for Paper, 'S' for Scissors\nRock beats Scissors, Scissors beat Paper, Paper beats Rock\n'Y' to play a new game, 'N' to quit, 'E' to exit\nif you win 3 rounds you win the game\n************************************************")

#Rock > Scissors
#Scissors > Paper
#Paper > Rock

def play():
    answer = input("Would you like to play a new game? 'Y' for Yes, 'N' for No, 'E' to exit\n")
    answer = answer.upper()
    
    if answer == "N":
        print("Ok, come back when you want to play.\n**********************************************************")
        return
    
    elif answer == "E":
        print("Goodbye!\n**********************************************************")
        exit()
    
    if answer == "Y":
        game_counter = 1
        user_wins = 0
        computer_wins = 0
        
        while True:
            while True:
                user = input(f"Game {game_counter} \nWhat's your choice? 'R' for Rock, 'P' for Paper, 'S' for Scissors\n")
                user = user.upper()
                
                if user not in ["R", "P", "S"]:
                    print("You entered an incorrect character, please try again.")
                    continue
                
                if user == "S":
                    user = "Scissors"
                elif user == "R":
                    user = "Rock"
                elif user == "P":
                    user = "Paper"
                
                computer = random.choice(['Rock', 'Paper', 'Scissors'])
                print(f"Game {game_counter} \nUser's Choice: {user} \nComputer's Choice: {computer}\n")
                
                if user == computer:
                    print("It's a tie!\n**********************************************************")
                elif is_win(user, computer):
                    print("You won this game!\n**********************************************************")
                    user_wins += 1
                else:
                    print("You lost this game :(\n**********************************************************")
                    computer_wins += 1
                
                print(f"{game_counter}.Game Score: You - {user_wins}, Computer - {computer_wins}\n")
                
                if user_wins == 3:
                    print(f"Congratulations, you won Game {game_counter}! You won {user_wins} rounds, Computer won {computer_wins} rounds.\n**********************************************************")
                    break
                elif computer_wins == 3:
                    print(f"Sorry, you lost Game {game_counter}! You won {user_wins} rounds, Computer won {computer_wins} rounds.\n**********************************************************")
                    break
            
            play_again = input("Play again? 'Y' for Yes, 'N' for No\n")
            if play_again.upper() == "Y":
                print("Time For Revenge")
                game_counter += 1
                user_wins = 0
                computer_wins = 0
            else:
                print("Ok, come back when you want to play.\n**********************************************************")
                break

def is_win(player, opponent):
    if (player == 'Rock' and opponent == 'Scissors') or (player == 'Scissors' and opponent == 'Paper') or (player == 'Paper' and opponent == 'Rock'):
        return True
    else:
        return False

play()