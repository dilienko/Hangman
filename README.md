# Hangman
This classic hangman game is implemented using python without third party libraries
Gameplay: 
You have to guess the hidden word. For each turn of the game, you try to guess one letter. If this letter is in the word, it will appear in the hidden word. In that case, in that case you get 10 points. If you guessed two or more letters in a row, you will be awarded 20 points. If you did not guess the letter, you lose one attempt (You have 10 attempts in total), and an additional element of the gallows and the hanged man appears in the picture. You can also use one hint per game (typing "help"), but in this case you lose half the points. You can also leave the game (typing "quit"). After losing or winning, you can leave the game or continue (your points are saved)

Used technologies:
Python without third-party libraries. Built-in modules were used (random, os, re)

Possible additions:
1. Improved output to the console
2. Add categories of word difficulty
3. Add multiplayer
