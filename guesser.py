

class Guesser():

    def __init__(self):
        self.guesses=[]

    def check_occurence(self,guess):
        if guess in self.guesses:
            return False
        else:
            self.guesses.append(guess)
            return True


    def make_a_guess(self):
        '''will only accept a guess that is comprised of only one letter.
        programmed to output appropriate message
        if user inputs a number or more than one letter at a time
        loops until the above criteria are met'''
        while True:
            guess=input("Make a guess:\n").lower()
            if len(guess)==1:
                if not guess.isdigit():
                    if self.check_occurence(guess):
                        if guess.isalnum():

                            return guess
                        else:
                            print("Input is not appropriate.\n"
                                  "Please choose a letter from the english alphabet!!\n")
                    else:
                        print("Already guess this letter!!\nSkipping a go!!\n")
                else:
                    print("The input was a number!!\n"
                          "Please enter a letter to make a guess!!\n")
            else:
                print("You have typed more than one letter!\n"
                      "Skipping a round!!")