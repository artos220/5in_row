from flask import Flask, render_template, request

from Game import Game
from Board import Board
from Player import Player


size = 15  # int(input('set field:'))  # board size
board = Board(size=size)

player1 = Player(player_id=1, name='Bob', size=size)
player2 = Player(player_id=2, name='Sara', size=size)
game = Game(board, [player1, player2])
# game.start()

app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST' and request.form.get('new_game'):
        game.restart()

    elif request.method == 'POST' and not game.game_over:
        r = request.form.to_dict()
        lst = [list(r)[0], r[list(r)[0]]]
        game.make_iteration(game.current_player, lst[0].split()[1], lst[0].split()[0])

    return render_template('index.html',
                           board=board.field,
                           player=game.current_player.player_id,
                           game_over=game.game_over)


if __name__ == '__main__':
    app.run(debug=True)
