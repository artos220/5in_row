import numpy as np
from Game import Game
from Board import Board
from Player import Player

size = int(input('set field:'))
playfield = Board(size=size)
playfield.show()

player1 = Player(player_id=1, name='Bob')
player2 = Player(player_id=2, name='Sara')
game = Game(playfield, [player1, player2])


def iteration(player: Player):
    playfield.show()

    while True:
        x, y = input('input coordinates x y:').strip().split()
        status = game.move(player.player_id, int(x), int(y))
        if status == 'WIN':
            print(player.name + ' WIN!')
            return False
        return True


repeat = True
while repeat:
    print(player1.name + ' move')
    repeat = iteration(player1)

    if not repeat:
        break

    print(player2.name + ' move')
    repeat = iteration(player2)
