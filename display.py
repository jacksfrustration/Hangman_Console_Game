from art import lives

class Display():

    def __init__(self):
        self.output=[]
        self.lives_index=0
        self.score=0
        self.total_matches=0
        self.highest_score=self.read_highest_score()

    def read_highest_score(self):
        try:
            with open("high_score.txt","r") as file:
                saved_score=int(file.read())
        except FileNotFoundError:
            with open("high_score.txt","w") as file:
                file.write(str(0))
            saved_score=0
        finally:
            return saved_score

    def update_high_score(self,score):
        with open("high_score.txt","w") as file:
            file.write(str(score))

    def initialize_display(self,word):
        for _ in range(len(word)):
            self.output.append("_")

    def display_game_state(self):
        print(f"{self.output}\n"
              f"{lives[self.lives_index]}\n")

    def update_display(self,letter,lst):
        for i,let in enumerate(lst):
            if let==letter:
                letter_index = i
                self.output[letter_index] = letter

    def update_lives(self):
        self.lives_index+=1

    def update_score(self):
        self.score+=1

    def display_win(self, chosen_word):
        self.total_matches+=1
        print(f"You win!!\n"
              f"The word was {chosen_word}!!\n"
              f"You had {self.lives_index} lives left\n"
              f"You have a score of {self.score}/{self.total_matches}\n"
              f"Highest score is: {self.highest_score}")

    def display_loss(self,chosen_word):
        print(lives[self.lives_index])
        self.total_matches += 1

        print("You ran out of lives.\nYou lose!!\n"
              f"You have a score of {self.score}/{self.total_matches}\n"
              f"Your highest score is: {self.highest_score} \n")
        print(f"The word was {chosen_word}!!")




    def reset_game(self):
        self.output.clear()
        self.lives_index = 0


