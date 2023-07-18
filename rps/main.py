"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""

human_player_move = ''


class Player:
    my_move = ''
    their_move = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):

    def move(self):
        while True:
            choice = input("Choose between rock/paper/scissors: ").lower()
            if choice in moves:
                global human_player_move
                human_player_move = choice
                return choice
            elif choice == "exit":
                quit()
            else:
                print("Please choose between rock/paper/scissors.")

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        global human_player_move
        return human_player_move

    def learn(self, my_move, their_move):
        pass


class CyclePlayer(Player):

    def move(self):
        if self.their_move == 'rock':
            self.their_move = 'paper'
            return 'paper'
        if self.their_move == 'paper':
            self.their_move = 'scissors'
            return 'scissors'
        else:
            self.their_move = 'scissors'
            self.their_move = 'rock'
            return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    if one == two:
        return "tie"
    elif ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return "win"
    else:
        return "lose"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) == "tie":
            pass
        elif beats(move1, move2) == "win":
            self.p1_score += 1
        else:
            self.p2_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        round_count = input("How many rounds would you like to play? ")
        if round_count.isnumeric():
            new_round = int(round_count)
            if round_count == 'exit':
                quit()
            else:
                print("Game start!")
                for game_round in range(new_round):
                    print(f"Round {game_round + 1}:")
                    self.play_round()
                    print(f"Score: P1 = {self.p1_score}, P2 = {self.p2_score}")
                    print('\n')
                print(f"Score is: P1 = {self.p1_score}, P2 = {self.p2_score}")
                if self.p1_score > self.p2_score:
                    print("Player 1 wins")
                elif self.p1_score < self.p2_score:
                    print("Plater 2 wins")
                else:
                    print("It's a Tie")
                print("Game over!")
        else:
            print("Please input a valid number.")
            game.play_game()


if __name__ == '__main__':
    enemy_options = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    game = Game(HumanPlayer(), random.choice(enemy_options))
    game.play_game()
