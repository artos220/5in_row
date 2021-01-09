from Game import Game
from Board import Board
from Player import Player

size = int(input('set field:'))  # board size
board = Board(size=size)

player1 = Player(player_id=1, name='Bob', size=size)
player2 = Player(player_id=2, name='Sara', size=size)
game = Game(board, [player1, player2])
game.start()
