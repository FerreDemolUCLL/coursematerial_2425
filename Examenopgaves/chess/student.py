class Piece:
    def __init__(self, code):
        self.code = code
        self.kind = code[0]
        self.player = code[1]

class Board:
    def __init__(self):
        self.board = {}
        self.initialize_board()

    def initialize_board(self):
        initial_positions = {
            'a1': 'Rw', 'b1': 'Nw', 'c1': 'Bw', 'd1': 'Qw', 'e1': 'Kw', 'f1': 'Bw', 'g1': 'Nw', 'h1': 'Rw',
            'a2': 'pw', 'b2': 'pw', 'c2': 'pw', 'd2': 'pw', 'e2': 'pw', 'f2': 'pw', 'g2': 'pw', 'h2': 'pw',
            'a7': 'pb', 'b7': 'pb', 'c7': 'pb', 'd7': 'pb', 'e7': 'pb', 'f7': 'pb', 'g7': 'pb', 'h7': 'pb',
            'a8': 'Rb', 'b8': 'Nb', 'c8': 'Bb', 'd8': 'Qb', 'e8': 'Kb', 'f8': 'Bb', 'g8': 'Nb', 'h8': 'Rb'
        }
        for position, code in initial_positions.items():
            self.set_piece(Piece(code), position)

    def set_piece(self, piece, position):
        self.board[position] = piece

    def get_piece(self, position):
        return self.board.get(position, None)

    def move_piece(self, start, end):
        if start not in self.board:
            raise ValueError("Illegal move: no piece at start position")
        piece = self.board[start]
        if end in self.board and self.board[end].player == piece.player:
            raise ValueError("Illegal move: cannot move to friendly territory")
        self.board[end] = piece
        del self.board[start]

    def display_board_state(self):
        board_str = ""
        for row in range(8, 0, -1):
            row_str = f"{row}: "
            for col in 'abcdefgh':
                position = f"{col}{row}"
                piece = self.get_piece(position)
                row_str += f"{piece.code if piece else '   '} | "
            board_str = board_str.rstrip(' | ') + "\n"
        board_str += "    a    b    c    d    e    f    g    h"
        return board_str

    def process_movements(self, movements):
        for start, end in movements:
            self.move_piece(start, end)

    def save_state(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.display_board_state())

def read_movement_file(file_name):
    movements = []
    with open(file_name, 'r') as file:
        for line in file:
            start, end = line.strip().split(" - ")
            movements.append((start, end))
    return movements

def process_chess_moves(movement_file_name, output_file_name):
    board = Board()
    movements = read_movement_file(movement_file_name)
    board.process_movements(movements)
    board.save_state(output_file_name)