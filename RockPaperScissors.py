import random

class game():
    
    def __init__(self):
        self.num_wins = 0
        self.num_losses = 0
        self.num_ties = 0
    
    def run_game(self):

        choices = ["paper", "scissors", "rock"]
    
        user_move = input("Please choice scissors, paper or rock: ")
        while user_move not in choices:
            user_move = input("Please choice scissors, paper or rock: ")
        comp_move = random.choice(choices)

        if user_move == comp_move:
            play.num_ties += 1
            print(f"BOTH with {user_move} - TIE")
        elif choices[(choices.index(user_move) + 1) % len(choices)] == comp_move:
            play.num_losses += 1
            print(f"COMPUTER with {comp_move} - WIN!")
        else:
            play.num_wins += 1
            print(f"USER with {user_move} - WIN!")
        
        return play.num_wins, play.num_losses, play.num_ties

    def print_results():
        print("You win %d times!" % play.num_wins)
        print("You lose %d times!" % play.num_losses)
        print("You tie %d times!" % play.num_ties)


if __name__ == "__main__":
    play = game()
    end = ""
    while end.lower() != "y":
        
        play.run_game()
        end = input("Enter 'y'/'Y' to continue ")
    game.print_results()
    play.num_wins, play.num_losses, play.num_ties = 0, 0, 0
