import random

class Game:

    RANDOM_NUMBER = random.randint(0,99)
    score = 100
    tries = 10

    def welcome_message(self):
        print('''
            Welcome!
            In this game you have to guess what's the secret number (0-99).

            RULES:
            1. You have ten turns to obtain the right choice. Otherwise you'll lose.
            2. You have a maximum inital score of 100.
            3. For each turn you fail, your score will down by 10.
            4. Get fun.
            Good luck :D
            ''')

    def show_user_score(self, game_state="current"):
        print("** Your {} score is: [{}] **".format(game_state, self.score))
    
    def show_remainig_tries(self):
        print("Ties: ", self.tries)

    def show_random_word(self):
        words = ['Wrong!', "Nop, that wasn't the word", "Try again", "Nice try", "You were closed", "Do not surrender yet", "Nop"]
        index = random.randint(0,len(words)-1)
        print("Error --> {} \n".format(words[index]))

    def check_answer(self, user_answer: int) -> bool:
        if (self.RANDOM_NUMBER == user_answer):
            return True
        
        self.score -= 10
        self.show_random_word()
        return False
            

    def start(self):
        try:
            self.welcome_message()
            victory = False
            print(self.RANDOM_NUMBER)
            while(self.tries > 0 and victory == False):
                self.show_user_score()
                self.show_remainig_tries()
                self.tries-=1
                user_number = input("Enter a number: ")
                victory = self.check_answer(int(user_number))
            else:
                print("\n","YOU WON!" if victory else "YOU LOSE...")
                self.show_user_score("final")

        except ValueError: # bad user input
            print("Invalind number")

game = Game()
game.start()
