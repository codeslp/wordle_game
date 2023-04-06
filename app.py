from rich.console import Console
from rich.table import Table
import table_logic as tablogic
from wordles import wordles
import random


title_table = Table(style = "white on green4", show_lines = True, show_header= False)
title_table.add_column(justify = "center")
title_table.add_column(justify = "center")
title_table.add_column(justify = "center")
title_table.add_column(justify = "center")
title_table.add_column(justify = "center")
title_table.add_row("W", "O", "R", "D", "L", "E")

Console().print(title_table)
print("")
Console().print("You have six tries to guess the five letter wordle!\n", style= "white on magenta")
Console().print("Letters you guess that are in the correct place will be in green.\n", style= "black on green4")
Console().print("Letters you guess that are in the word, but not in the correct place will be in yellow.\n", style= "black on yellow3")
Console().print("Letters you guess that not in the word will have no color.\n")
Console().print("Good luck!\n", style= "white on magenta")



wordle = random.choice(wordles)

checked_table_list = []

total_guesses = int(0)
play_again = True


empty_table = Table(style = "white", show_lines = True, show_header= False)
empty_table.add_column(justify = "center")
empty_table.add_column(justify = "center")
empty_table.add_column(justify = "center")
empty_table.add_column(justify = "center")
empty_table.add_column(justify = "center")
empty_table.add_row("_", "_", "_", "_", "_")

for i in range(6 - total_guesses):
    Console().print(empty_table)

while play_again == True:

    guess = str(input("Make a guess: "))
    guess = guess.upper()


    if len(guess) != 5 and total_guesses < 6:
        print("Your guess must be five letters long. Try again!")
        continue
    elif guess.isalpha() == False and total_guesses < 6:
        print("Your guess must be letters only. Try again!")
        continue
    elif guess.isalpha() == True and len(guess) == 5 and total_guesses < 6:
        total_guesses += 1
        attempt_table = tablogic.AttemptTable(guess)
        guess_list = []
        for i in guess:
            guess_list.append(i)
        guess_table = attempt_table.make_table(guess_list, wordle)
        checked_table_list.append(guess_table)
        Console().print(title_table)
        for i in checked_table_list:
            Console().print(i)
        for i in range(6 - total_guesses):
            Console().print(empty_table)
        if guess == wordle:
            Console().print("\n:partying_face: You win!")
            print("The wordle was", wordle, "!")
            play_again = str(input("Would you like to play [again? (y/n): ").lower())
            if play_again == "y":
                play_again = True
            elif play_again == "n":
                play_again = False
        elif guess != wordle and total_guesses == 6:
            Console().print("You lose! :poop: The wordle was", wordle, "!")
            play_again = str(input("Would you like to play [again? (y/n): ").lower())
            if play_again == "y":
                play_again = True
            elif play_again == "n":

                play_again = False
        continue






