import unittest
from game import Board
class TestSuite(unittest.TestCase):
    def test_we_can_multiply(self):
        assert (6 * 7) == 42
    
    def test_there_is_a_board(self):
        blank_board = Board()
        self.assertEqual(blank_board.board, [[0,0,0],[0,0,0],[0,0,0]])
        
    def test_board_can_have_tile_added_in_middle(self):
        board = Board()
        tile_type = 1 # White
        board.add_tile(tile_type, row=1, column=1)
        self.assertEqual(str(board), "...\n.W.\n...")
        
    def test_if_three_in_a_row_wins(self):
        board = Board()
        tile_type = 1 # White
        board.add_tile(tile_type, row=1, column=1)
        board.add_tile(tile_type, row=1, column=0)
        board.add_tile(tile_type, row=1, column=2)
        self.assertEqual(board.three_in_a_row, True)
        
    def test_is_not_three_in_a_row_fails(self):
        board = Board()
        tile_type = 1 # White
        self.assertEqual(board.three_in_a_row, False)
        
    def test_transpose(self):
        board = Board()
        tile_type = 1 # White
        board.add_tile(tile_type, row=1, column=1)
        board.add_tile(tile_type, row=1, column=0)
        board.add_tile(tile_type, row=1, column=2)
        #board.transpose()
        self.assertEqual(str(board), "")
        
        
 class Board():
    def __init__(self):
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        return 
    
        
    
    def add_tile(self, tile_type=1, row=0, column=0):
       self.board[row][column] = tile_type
       return self.board

    def __str__(self):
        b = ""
        for i in range(3):
            if i > 0:
                b += '\n'
            for j in range(3):
                if self.board[i][j] == 0:
                    b += "."
                elif self.board[i][j] == 1:
                    b += "W"
                else:
                    b += "B"
        return b
    
    @property
    def three_in_a_row(self):
        for i in range(3):
            if sum(self.board[i]) >= 3:
                return True
        
        return False    

