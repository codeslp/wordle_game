# Introduction to Python Wordle Console Game
## by Brian Farish

This is a console-based implementation of the game Wordle. It uses the rich libraries (https://github.com/Textualize/rich) to create tables, color fields, and emojis. 

The game allows the player to make six guesses to discover a secret random five letter word, and displays the guesses in a table in yellow, if the letter is in the word, in green, if the letter is in the word and in the right position, and uncolored, if the letter is not in the word.  

# Design and Implementation

I wanted to imitate a feeling of playing the game with the empty tables displayed each time to give a sense of status and progress to the player. I used rich, because it could create the tables and the colors I needed. The logic of the game is very simple, really, so I wanted to challenge myself to create something slightly more visually engaging than just coloring the letters and listing them.

I found that creating and populating the tables was by far the most complex part of this project. I do see now that it could have been accomplished without the class AttemptTable. I created this at the start, knowing that I would have to make tables, but not knowing exactly how I would end up doing it, so I laid the foundation with the class and its methods. 

Because this was my first implementation of OOP, without any basic framework to guide me, I found that conceptually deciding how much of the logic of the game needed to be in app.py and how much needed to be in table_logic.py was another challenge. I tried to abstract away into the methods as much as I could. But I do not know if this is necessary. Ultimately, it is, I think, better to write what is necessary and efficient, rather than to structure something in a certain way simply as a challenge. But it is impossible to discover what is necessary and efficient, without making mistakes.

## One thing that I banged my head against over and over was working out one bug. 
The loop in table_logic kept discovering the first correctly placed character, and then ignoring the rest of the player's guess and returning tables full of the correct guess. This was because of how it looped through.    The if/elif logic nested in the for loop in table_logic.py returned only that value after it was discovered, because that value was there each time it looped. I tried MANY ways of looping to try to get past it. But ultimately I could only get it to move on by replacing the searched and sorted character with a filler character ("@"). That worked. There is probably a better way of doing this, but I did not discover it. 

# Conclusions

Working out the problem in my for loop with the nested logic was definitely an instructive experience in how for loops iterate. The list does not vanish after I have found what I want from it!

The way that I found my mistake was by methodically going through each step and printing the status of my variables in each point. It is tedious, but it is a good way to debug that my patient and methodical instructor, Terrance Greene (https://www.linkedin.com/in/terrance-greene-b9172a83/) taught me.

The above method was part of my solution, but I also learned that you have to walk away from the project for a bit and come back. The solution came after I had left the project for a day, and was working on learning some fundamentals about sort and search algorithms. I was coding a simple linear search algo, and the solution popped into my mind. Rest and staying sharp on fundamentals are a central part of the work of coding.

If I come back to this, it will be to implement an actual front-end to the game. I could not stop thinking about how much better the game would be if I was using some actual styling tools.
