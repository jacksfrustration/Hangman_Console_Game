from art import lives, logo
from words import Words
from display import Display
from guesser import Guesser


words = Words()
display = Display()
guesser = Guesser()

def initialize_game():
    '''Initialize the game by choosing a word and setting up the display.'''
    words.chosen_word = words.choose_a_word()
    guesser.guesses.clear()
    display.initialize_display(words.chosen_word)
    display.lives_index=0

def play_game():
    '''Run a single game session.'''
    while "_" in display.output and display.lives_index < len(lives) - 1:
        display.display_game_state()
        guessed_letter = guesser.make_a_guess()

        if guessed_letter in words.chosen_word:
            display.update_display(letter=guessed_letter,lst=list(words.chosen_word))
        else:
            display.update_lives()
            print(f"You guessed wrong.\n "
                  f"{guessed_letter} is not in the word. \n"
                  f"You have {len(lives) - 1 - display.lives_index} lives left!")

    if "_" not in display.output:
        display.update_score()
        display.display_win(chosen_word=words.chosen_word)
        display.update_highest_score()
    else:
        display.reset_game()
        display.display_loss(chosen_word=words.chosen_word)

def main():
    '''Main game loop'''
    print(logo)
    while True:
        initialize_game()
        play_game()

        play_again = input("Play again? (yes/no): ").lower()
        while play_again not in ("yes", "no"):
            play_again = input("Invalid input. Play again? (yes/no): ").lower()

        if play_again.startswith("n"):
            break
        else:
            display.reset_game()

if __name__ == "__main__":
    main()