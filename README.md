# Hex Game

An application that can be used to play a variation of the [Hex game](https://en.wikipedia.org/wiki/Hex_(board_game) "About Hex"). It has Player vs Player, Computer vs Player and Computer vs Computer options.

![image](https://user-images.githubusercontent.com/30511514/183648226-48508fca-b5d5-428c-b92c-b3aba9ebe775.png)

## The rules

There are two players. A player picks the red color and the one picks the red color. Does not matter wich color starts first. Each turn the player places a piece of their representative color on an empty space on the table. The purpose of the game is for blue to connect a bath of hexes from the left side of the table to the right, and for red to connect the top side of the table to the bottom.

## Functionalities

🔹 When you run the app, the first thing it asks is the settings for the game: how big the table do you want to have, the game mode (pvp, pve, eve), witch color the player picks (in pve) etc.

![image](https://user-images.githubusercontent.com/30511514/183647095-85061e56-dcba-4eae-81f6-bddcd7d8a700.png)

🔹 After that the map (graphical interface) appears in a different window.

![image](https://user-images.githubusercontent.com/30511514/183647195-9088e122-1548-4d28-b85b-37adc40e460c.png)

🔹 At each step the map is updated in the graphical interface and in the console.

![image](https://user-images.githubusercontent.com/30511514/183647870-521529f7-dec6-4b12-99cc-55acb8ffa11b.png)

🔹 When the game ends or the window is closed there are stats written in the project console.

![image](https://user-images.githubusercontent.com/30511514/183647963-4f5f8294-a9c6-493c-9a62-12a642f9b139.png)

🔹 Pressing 'r' resets the game back to the original state (just after the settings were made).

## Artificial Intelligence

The algorithm has Player vs Player, Player vs Computer and Computer vs Computer modes. For the last 2, there are additional settings that need to be done. The computer can use [Min-Max algorithm](https://en.wikipedia.org/wiki/Minimax "More about the Min-Max algorithm") or [Alpha-Beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning "More about Alpha-Beta pruning"). The user of the app can also select the "difficulty" of the AI, wich sets the depth of the algorithm (a higher difficulty means a greater depth).

## Heuristics Used

For the Min-Max and Alpha-Beta to work we need an heuristic that estimates the score of a game state.

🔹 For the first heurisitc I made something like a Breadth First Search, but with jumps over the white hexes, the more white hexes jumped, lower the score. The score is given by the path from one side to the other that as the fewest missing (white) hexes.

🔹 For the second heurisitc I wanted a score function that rises when the current player has more columns (blue) / rows (red) with pieces on them, and the more he has on that line, the greater the score. So the AI should focus on getting as many columns (blue) / lines (red) and as less pieces on those lines, so the result should be close to one straight line from one side to the other.


