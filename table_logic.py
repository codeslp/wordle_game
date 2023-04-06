from rich.table import Table


class AttemptTable:
    def __init__(self, guess):
        self.table = Table(show_lines = True, show_header = False)
        self.guess = guess
        

    def make_table(self, guess_list, wordle):
        row_list = []
        i = 0

        for i, letter in enumerate(guess_list):
            if letter in wordle and guess_list.index(letter) == wordle.index(letter):
                self.table.add_column(justify = "center", style = "black on green4")
                row_list.append(letter)
                #this is here to keep the search algo from discovering repeated characters.
                guess_list[i] = "@"
            elif letter in wordle: 
                self.table.add_column(justify = "center", style = "black on yellow3")
                row_list.append(letter)
                guess_list[i] = "@"
            else:
                self.table.add_column(justify = "center")
                row_list.append(letter)
                guess_list[i] = "@"

        self.table.add_row(row_list[0], row_list[1], row_list[2], row_list[3], row_list[4])
        return self.table
