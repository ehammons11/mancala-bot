# mancala-bot
This project is my dive into mini-max algorithms though a two-player marble based game called mancala. 

In this project, the player is able to run the file MancalaMain.py and play against an AI opponent. The opponent is using the mini-max algorithm with alpha-beta pruning, and a heuristic function that analyzes the board to determine what the relative "score" is. He is a force to be reckoned with. 

The rules of the game are determined by the class file MancalaClass.py. The rule of the classic game can be found here https://endlessgames.com/wp-content/uploads/Mancala_Instructions.pdf. It sets the parameters for the game and has a function that sees all of the next possible moves in a given position, which is what powers the mini-max algorithm's ability to build its search tree. 

The mini-max determines the relative score of the board using the function getScore in MancalaClass.py. There are two variables, a and b, that change what the heuristic is for the opponent. a is the weight of the actual score pot on a players side, while b is the weight of all the other marbles on a players side. The reason b is necessary is because of the rules of Mancala is that if your side has no marbles, the opponent gets to keep all of the marbles on their side. A good strategy is to keep lots of marbles on your own side, so the AI values positions based on all marbles, not just the score marbles. 

The AI can run as slow or as fast as you want, which will also change the difficulty. You can change the variable max_time in MancalaMain.py in order to play quicker games or make the AI harder. Feel free as well to expieriment with the getScore function. 
