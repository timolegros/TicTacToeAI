from os import system
import time
from math import inf as infinity


class TicTacToe:
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def drawBoard(self):
        print(' ', self.board[0], '|', self.board[1], '|', self.board[2], ' ')
        print('----------------')
        print(' ', self.board[3], '|', self.board[4], '|', self.board[5], ' ')
        print('----------------')
        print(' ', self.board[6], '|', self.board[7], '|', self.board[8], ' ')

    def drawUpdatedBoard(self, board):
        print(' ', board[0], '|', board[1], '|', board[2], ' ')
        print('----------------')
        print(' ', board[3], '|', board[4], '|', board[5], ' ')
        print('----------------')
        print(' ', board[6], '|', board[7], '|', board[8], ' ')

    def emptySpots(self):
        """Makes a list containing the indexes of all the free/open positions on the board."""
        result = []
        for i, j in enumerate(self.board):
            if j == ' ':
                result.append(i)

        return result

    def winner(self, player):
        """ Tells you if the player you are checking for has won the game. For example if player 1 has 3 in a row but
        player 2 is checking if he himself won, the function will return False."""
        i = 0
        while i < 9:
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True
            else:
                i += 3

        i = 0
        while i < 3:
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
            else:
                i += 1

        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        elif self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def evaluate(self):
        if self.winner('O'):
            score = +1
        elif self.winner('X'):
            score = -1
        else:
            score = 0

    def boardFull(self):
        counter = 0
        for i in self.board:
            if i == ' ':
                counter += 1
        return not (counter >= 1)

    def gameOver(self):
        return self.winner('X') or self.winner('O') or self.boardFull()

    def clean(self):
        system('cls')

    def humanTurn(self, player):
        depth = len(self.emptySpots())

        if depth == 0 or self.gameOver():
            return

        move = -1

        while move < 1 or move > 9:
            # clean()
            print("Human turn")
            self.drawBoard()
            move = int(input('Enter a position between 1 and 9: '))

            if 9 >= move >= 1:
                if self.board[move - 1] == ' ':
                    move -= 1
                    if player == 'X':
                        self.board[move] = 'X'
                    else:
                        self.board[move] = 'O'
                    self.drawBoard()
                    return
                else:
                    print('This position is not free')
                    move = -1
                    time.sleep(1)
            else:
                print('Bad move')
                move = -1


class ArtificialIntelligence:

    def __init__(self, board):
        self.board = board
        self.score = None

    def winner(self, player):
        """ Tells you if the player you are checking for has won the game. For example if player 1 has 3 in a row but
        player 2 is checking if he himself won, the function will return False."""
        i = 0
        while i < 9:
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True
            else:
                i += 3

        i = 0
        while i < 3:
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
            else:
                i += 1

        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        elif self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    def boardFull(self):
        counter = 0
        for i in self.board:
            if i == ' ':
                counter += 1
        return not (counter >= 1)

    def emptySpots(self):
        """Makes a list containing the indexes of all the free/open positions on the board."""
        result = []
        for i, j in enumerate(self.board):
            if j == ' ':
                result.append(i)

        return result

    def gameOver(self):
        return self.winner('X') or self.winner('O') or self.boardFull()

    def evaluate(self):
        if self.winner('O'):
            self.score = +1
            return self.score
        elif self.winner('X'):
            self.score = -1
            return self.score
        else:
            self.score = 0
            return self.score

    def minimax(self, board, depth, player):
        if player == 'O':
            best = [-1, -infinity]
        else:
            best = [-1, infinity]

        if depth == 0 or self.gameOver():
            self.score = self.evaluate()  # checks who winner is - returns a 1, -1, or 0 for tie
            return [-1, self.score]

        for spot in self.emptySpots():
            # changes the blank spot on the board at index (spot) to X or O depending on the turn
            self.board[spot] = player

            if player == 'O':
                self.score = self.minimax(self.board, depth - 1, 'X')
            else:
                self.score = self.minimax(self.board, depth - 1, 'O')

            self.board[spot] = ' '
            self.score[0] = spot

            if player == 'O':
                if best[1] < self.score[1]:
                    best = self.score
            else:
                if best[1] > self.score[1]:
                    best = self.score

        return best

    def AImove(self, lengthEmpty, gameOver):
        """ lengthEmpty has to be self.emptySpots(self.board) and gameOver is self.gameOver(self.board)"""
        depth = len(lengthEmpty)
        if depth == 0 or gameOver:
            return
        copyBoard = []
        for i in self.board:
            copyBoard.append(i)

        print("AI turn")
        move = self.minimax(copyBoard, depth, 'O')
        print(move)
        self.board[move[0]] = 'O'
        return self.board



def main():

    game = TicTacToe()

    game.drawBoard()

    while not (game.gameOver()):
        game.humanTurn('X')
        AI = ArtificialIntelligence(game.board)
        move = AI.AImove(game.emptySpots(), game.gameOver())
        game.drawUpdatedBoard(move)

    if game.winner('X'):
        print('Player 1 Wins!')
    elif game.winner('O'):
        print('Player 2 Wins!')
    elif game.boardFull():
        print('Its a Tie')


main()
