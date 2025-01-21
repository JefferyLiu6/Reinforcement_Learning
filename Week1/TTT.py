class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def reset(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for i in range(3):
            row = self.board[i * 3:(i + 1) * 3]
            print(f"| {row[0]} | {row[1]} | {row[2]} |")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diag1]):
                return True

            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diag2]):
                return True

        return False

    def empty_squares(self):
        return " " in self.board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def is_full(self):
        return not self.empty_squares()

    def check_draw(self):
        return self.is_full() and self.current_winner is None

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class ComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return 4

        for move in game.available_moves():
            game.make_move(move, self.letter)
            if game.current_winner == self.letter:
                game.board[move] = " "
                return move
            game.board[move] = " "

        opponent = "O" if self.letter == "X" else "X"
        for move in game.available_moves():
            game.make_move(move, opponent)
            if game.current_winner == opponent:
                game.board[move] = " "
                return move
            game.board[move] = " "

        return game.available_moves()[0]

# Play a human-vs-human game
def play_game_human_vs_human():
    game = TicTacToe()
    player_x = HumanPlayer("X")
    player_o = HumanPlayer("O")

    game.print_board()

    while game.empty_squares():
        for player in [player_x, player_o]:
            move = player.get_move(game)
            if game.make_move(move, player.letter):
                game.print_board()
                if game.current_winner:
                    print(f"{player.letter} wins!")
                    return
                elif game.check_draw():
                    print("It's a draw!")
                    return

# Play a human-vs-computer game
def play_game_human_vs_computer():
    game = TicTacToe()
    human = HumanPlayer("X")
    computer = ComputerPlayer("O")

    game.print_board()

    while game.empty_squares():
        for player in [human, computer]:
            move = player.get_move(game)
            if game.make_move(move, player.letter):
                game.print_board()
                if game.current_winner:
                    print(f"{player.letter} wins!")
                    return
                elif game.check_draw():
                    print("It's a draw!")
                    return

# Uncomment the desired function to play
play_game_human_vs_human()
# play_game_human_vs_computer()
