import conda
import numpy as np


class Mancala():
    def __init__(self):
        self.board = [
            [4, 4, 4, 4, 4, 4, 0],
            [4, 4, 4, 4, 4, 4, 0]
        ]
    
    def printBoard(self):
        try:
            fliped = []
            for i in range(6,-1,-1):
                fliped.append(self.board[0][i])
            print(fliped)
            print("  ", self.board[1])
        except:
            print(self.board)

    def setBoard(self, board):
        self.board = board

    def expandBoard(self, player): #player is an int, 1 for bottom player, 2 for top
        possibleTurns = []
        if player == 1:
            for i in range(0,6):
                goAgain = False
                tempBoard = [self.board[0].copy(), self.board[1].copy()]
                marbles = self.board[1][i]
                tempBoard[1][i] = 0
                if not marbles == 0:
                    for j in range(1,marbles + 1, 1):
                        if i + j <= len(self.board[1]) -1:
                            tempBoard[1][i + j] = tempBoard[1][i + j] + 1
                        elif i + j - 6 <= len(self.board[1]) - 1:
                            if not i + j - 7 == 6: 
                                tempBoard[0][i + j -7] = tempBoard[0][i + j - 7] + 1
                        elif i + j - 13 <= len(self.board[1]) - 1:
                            tempBoard[1][i + j - 13] = tempBoard[1][i + j - 13] + 1
                        if i + marbles == 6 or i + marbles - 13 == 6:
                            goAgain = True

                    if i + marbles < 6:
                        if self.board[1][i + marbles] == 0 and not self.board[0][abs(5-(i + marbles))] == 0:
                            tempBoard[1][6] += tempBoard[1][i + marbles] + tempBoard[0][abs(5-(i + marbles))]
                            tempBoard[0][abs(5-(i + marbles))] = 0
                            tempBoard[1][i + marbles] = 0
                    elif ((i + marbles - 13) < 6) and ((i + marbles - 13) >= 0):
                        if self.board[1][i + marbles - 13] == 0:
                            tempBoard[1][6] += tempBoard[1][i + marbles - 13] + tempBoard[0][abs(5-(i + marbles -13))]
                            tempBoard[0][abs(5-(i + marbles -13))] = 0
                            tempBoard[1][i + marbles - 13] = 0
                    tempGame = Mancala()
                    tempGame.setBoard(tempBoard)

                    if not tempGame.gameOver() == False:
                        goAgain = False
                    possibleTurns.append((tempGame.board, goAgain))
        elif player == 2:
            for i in range(0,6):
                goAgain = False
                tempBoard = [self.board[0].copy(), self.board[1].copy()]
                marbles = self.board[0][i]
                tempBoard[0][i] = 0
                if not marbles == 0:
                    for j in range(1,marbles + 1, 1):
                        if i + j <= len(self.board[0]) -1:
                            tempBoard[0][i + j] = tempBoard[0][i + j] + 1
                        elif i + j - 6 <= len(self.board[0]) - 1:
                            if not i + j - 7 == 6: 
                                tempBoard[1][i + j -7] = tempBoard[1][i + j - 7] + 1
                        elif i + j - 13 <= len(self.board[0]) - 1:
                            tempBoard[0][i + j - 13] = tempBoard[0][i + j - 13] + 1
                        if i + marbles == 6 or i + marbles - 13 == 6:
                            goAgain = True

                    if i + marbles < 6:
                        if self.board[0][i + marbles] == 0 and not self.board[1][abs(5-(i + marbles))] == 0:
                            tempBoard[0][6] += tempBoard[0][i + marbles] + tempBoard[1][abs(5-(i + marbles))]
                            tempBoard[1][abs(5-(i + marbles))] = 0
                            tempBoard[0][i + marbles] = 0
                    elif (i + marbles - 13 < 6) and (i + marbles - 13 >= 0):
                        if self.board[0][i + marbles - 13] == 0:
                            tempBoard[0][6] += tempBoard[0][i + marbles - 13] + tempBoard[1][abs(5-(i + marbles -13))]
                            tempBoard[1][abs(5-(i + marbles -13))] = 0
                            tempBoard[0][i + marbles - 13] = 0
                    tempGame = Mancala()
                    tempGame.setBoard(tempBoard)
                    tempGame.gameOver()

                    if not tempGame.gameOver() == False:
                        goAgain = False
                    
                    possibleTurns.append((tempGame.board, goAgain))            
        return possibleTurns

    def getScore(self, a, b): #player 1 is the maximizer, player 2 is the minimizer. a and b are constants to change the heuristic of the scoring method. 
        num1 = a*self.board[1][6]
        num2 = a*self.board[0][6]
        for i in range(6):
            num1 += b*self.board[1][i]
            num2 += b*self.board[0][i]
        return num1 - num2

    def neuralScore(self, neural_net):  # used for potential neural net class in the future.
        inputs = []
        for i in range(7):
            inputs.append(self.board[0][i])
        for i in range(7):
            inputs.append(self.board[1][i])
        neural_net.allforward(inputs)
        return neural_net.output[0][0]

    def userTurn(self, index): #index is the position of the list where the player wants to take a turn.
                i = index
                goAgain = False
                tempBoard = [self.board[0].copy(), self.board[1].copy()]
                marbles = self.board[1][i]
                tempBoard[1][i] = 0
                if not marbles == 0:
                    for j in range(1,marbles + 1, 1):
                        if i + j <= len(self.board[1]) -1:
                            tempBoard[1][i + j] = tempBoard[1][i + j] + 1
                        elif i + j - 6 <= len(self.board[1]) - 1:
                            if not i + j - 7 == 6: 
                                tempBoard[0][i + j -7] = tempBoard[0][i + j - 7] + 1
                        elif i + j - 13 <= len(self.board[1]) - 1:
                            tempBoard[1][i + j - 13] = tempBoard[1][i + j - 13] + 1
                        if i + marbles == 6 or i + marbles - 13 == 6:
                            goAgain = True

                    if i + marbles < 6:
                        if self.board[1][i + marbles] == 0 and not self.board[0][abs(5-(i + marbles))] == 0:
                            tempBoard[1][6] += tempBoard[1][i + marbles] + tempBoard[0][abs(5-(i + marbles))]
                            tempBoard[0][abs(5-(i + marbles))] = 0
                            tempBoard[1][i + marbles] = 0
                    elif (i + marbles - 13 < 6) and (i + marbles - 13 >= 0):
                        if self.board[1][i + marbles - 13] == 0:
                            tempBoard[1][6] += tempBoard[1][i + marbles -13] + tempBoard[0][abs(5-(i + marbles -13))]
                            tempBoard[0][abs(5-(i + marbles-13))] = 0
                            tempBoard[1][i + marbles - 13] = 0
                self.board = tempBoard
                return (tempBoard, goAgain)
    
    def gameOver(self):
        player1 = False
        player2 = False
        for i in range(6):
            if self.board[0][i] == 0:
                player2 = True
            else:
                player2 = False
                break
        if player2 == True:
            for i in range(0,6):
                self.board[1][6] += self.board[1][i]
                self.board[1][i] = 0
            return 2

        for i in range(6):
            if self.board[1][i] == 0:
                player1 = True
            else:
                player1 = False
                break      
        if player1 == True:
            for i in range(0,6):
                self.board[0][6] += self.board[0][i]
                self.board[0][i] = 0
            return 1

        return False      
