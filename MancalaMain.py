import conda
from MancalaClass import Mancala
import random
game = Mancala()
import time
print("-------------------------")
print("Welcome to MancalaBot!")
print("-------------------------")
game.printBoard()

counter = 0

def finalScore():
    print("The final score of the game was: ", game.getScore(1, 0))

def maximize_score(state, count, alpha, beta):
    global counter
    counter = counter + 1
    tempGame = Mancala()
    tempGame.setBoard(state)

    if count <= 0:
        return (tempGame.getScore(1.875, 1), state, False)
    if not tempGame.gameOver() == False:
        return (tempGame.getScore(1.875, 1), state, False)

    best_state = state
    goAgain = False
    score = float("-inf")

    expanded = tempGame.expandBoard(1)
    random.shuffle(expanded)


    for newState in expanded:
        newGame = Mancala()
        newGame.setBoard(newState[0])
        if newState[1] == True:
            for newerState in newGame.expandBoard(1):
                maximize = maximize_score(newerState[0], count - 1, alpha, beta)
                if maximize[0] > score:
                    score = maximize[0]
                    best_state = newState[0]
                    goAgain = True
        else:
            minimize = minimize_score(newState[0], count - 1, alpha, beta)
            if minimize[0] > score:
                score = minimize[0]
                best_state = newState[0]
                goAgain = False 

                if score > alpha:
                    alpha = score

                if score >= beta:
                    return(score, best_state, goAgain)                

    return (score, best_state, goAgain)

def minimize_score(state, count, alpha, beta):
    global counter
    counter = counter + 1
    tempGame = Mancala()
    tempGame.setBoard(state)

    if count <= 0:
        return (tempGame.getScore(1.875, 1), state, False)
    if not tempGame.gameOver() == False:
        return (tempGame.getScore(1.875, 1), state, False)
    best_state = state
    goAgain = False
    score = float("inf")

    expanded = tempGame.expandBoard(2)
    random.shuffle(expanded)

    for newState in expanded:
        newGame = Mancala()
        newGame.setBoard(newState[0])
        if newState[1] == True:
            for newerState in newGame.expandBoard(2):
                minimize = minimize_score(newerState[0], count - 1, alpha, beta)
                if minimize[0] < score:
                    score = minimize[0]
                    best_state = newState[0]
                    goAgain = True

        else:
            maximize = maximize_score(newState[0], count - 1, alpha, beta)
            if maximize[0] < score:
                score = maximize[0]
                best_state = newState[0]
                goAgain = False

            if score <= alpha:
                return(score, best_state, goAgain)

            if score < beta:
                beta = score

    return (score, best_state, goAgain)


while True:

    goAgain = True
    while goAgain == True:
        turn = input("Enter which set of marbles you want to move (1-6): ")
        if (turn == "") or (int(turn) < 0 or int(turn) > 6):
            print("Incorrect Input, Try again")
            continue
        print("-------------------------")
        goAgain = game.userTurn(int(turn) - 1)[1]
        game.printBoard()
        check_game = game.gameOver()
        if not check_game == False:
            break

    check_game = game.gameOver()
    if not check_game == False:
        break

    print("-------------------------")
    print("Now its MancalaBot's turn")
    goAgain = True
    while goAgain == True:
        max_time = 10                                                           #Change this max time variable to increase the difficulty of the bot or make it play faster. For really fast games, 1 second is low enough. 
        start_time = time.time()
        count = 7
        while (time.time() - start_time) < max_time:
            turn = minimize_score(game.board, count, float("-inf"), float("inf"))
            count += 1
        game.setBoard(turn[1])
        game.printBoard()
        check_game = game.gameOver()
        print("-------------------------")
        print("Number of expansions: ", counter)
        print("Depth: ", count-1)
        counter = 0
        if turn[2] == False:
            break
        if not check_game == False:
            break
        print("-------------------------")
        print("Now its MancalaBot's turn..... again")

    check_game = game.gameOver()
    if not check_game == False:
        break

print("-------------------------")
print("Final Board: ")
game.printBoard()
game.gameOver()

if game.getScore(1,0) > 0:
    print("Congrats! You just beat an AI at Mancala")
    finalScore()
elif game.getScore(1,0) < 0:
    print("Sorry :/ You lost to an Ai")
    finalScore()
else:
    print("Draw! Try again")
    finalScore()


