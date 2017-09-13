

class TicTacToe(object):

    win_with = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
        [1, 5, 9], [3, 5, 7]  # diagonals
    ]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.player1.set_symbol('X')
        self.player2.set_symbol('O')

        self.state = ['-'] * 9

        self.turn_p1 = True  # player1's turn
        self.finished = False

    def next_turn(self):
        # Make sure game is not finished
        assert not self.finished

        # Decide who's turn it is
        player = self.player1 if self.turn_p1 else self.player2

        # Ask player for move
        move = player.decide_move(self.state)

        # Check move for validity
        assert type(move) is int
        assert 1 <= move <= 9
        assert self.state[move - 1] == '-'

        # Perform move
        self.state[move - 1] = player.symbol

        # Check game state
        if self.check_state():
            self.finished = True

        # Switch turns
        self.turn_p1 = not self.turn_p1

    def check_state(self):
        def check_win(player):
            def has(x):
                return self.state[x - 1] == player.symbol

            for line in self.win_with:
                if all(has(x) for x in line):
                    player.win()
                    return True

        def check_draw():
            if all(s != '-' for s in self.state):
                print("It's a draw!")
                return True

        return check_win(self.player1) or check_win(self.player2) or check_draw()

    def _repr_html_(self):
        html = """
            <table>
                <tr>
                    <td>{0}</td>
                    <td>{1}</td>
                    <td>{2}</td>
                </tr>
                    <td>{3}</td>
                    <td>{4}</td>
                    <td>{5}</td>
                <tr>
                </tr>
                <tr>
                    <td>{6}</td>
                    <td>{7}</td>
                    <td>{8}</td>
                </tr>
            </table>
        """

        return html.format(*self.state)
