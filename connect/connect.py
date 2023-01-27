class ConnectGame:
    def __init__(self, board: str):
        self.board = [line.strip() for line in board.splitlines()]

    def get_winner(self):
        O_wins = True
        for row in self.board:
            if "O" not in row:
                O_wins = False
        if O_wins:
            return "O"
        return ""
