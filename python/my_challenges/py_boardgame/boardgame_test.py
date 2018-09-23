import unittest
import boardgame
from boardgame import Board, Dice, Player

class BoardGameTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1, 1)

    def test_board_has_12_squares(self):
        board = Board(12)
        self.assertEqual(len(board.squares), 12)

    def test_dice6_never_rolls_above_six(self):
        d = Dice()
        for i in range(100):
            x = d.roll
            print(x)
            self.assertTrue(x <= 6)

    def test_dice_rolls_all_numbers(self):
        d = Dice()
        rolls = []
        for i in range(500):
            x = d.roll
            rolls.append(x)
        print(rolls)
        self.assertIn(6, rolls)
        self.assertIn(5, rolls)
        self.assertIn(4, rolls)
        self.assertIn(3, rolls)
        self.assertIn(2, rolls)
        self.assertIn(1, rolls)

    def test_player_starts_with_1000(self):
        al = Player("Al")
        self.assertEqual(al.money, 1000)

    def test_player_starts_with_position_0(self):
        al = Player("Al")
        self.assertEqual(al.current_position, 0)

    def test_player_starts_with_money_1000(self):
        al = Player("Al")
        self.assertEqual(al.money, 1000)

    def test_move_player_moves_position(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(6, board)
        self.assertEqual(al.current_position, 6)


    def test_move_player_wraps_position(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(6, board)
        al.move_player(6, board)
        al.move_player(3, board)
        self.assertEqual(al.current_position, 3)

    def test_can_print_square_on_board(self):
        board = Board(12)
        square = board.squares[5]
        self.assertEqual(str(square), "Four Road, type = Property, status = Vacant, price = £250")

    def test_can_tell_vacant_property_if_landed_on(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(5, board)
        self.assertEqual(al.current_position, 5)
        self.assertEqual(al.current_position_print(board), "Four Road, type = Property, status = Vacant, price = £250")

    def test_player_can_buy_property(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(5, board)
        al.buy_property(board)
        square = board.squares[5]
        self.assertEqual(str(square), "Four Road, type = Property, status = Owned by Al, price = £250")
        
    def test_player_money_decreases_when_buy_property(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(5, board)
        al.buy_property(board)
        self.assertEqual(al.money, 750)

    def test_player_cannot_buy_owned_property(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(5, board)
        al.buy_property(board)
        fred = Player("Fred")
        fred.move_player(5, board)
        self.assertEqual(fred.buy_property(board), "Property is Owned by Al")

    def test_player_has_to_pay_rent_on_owned_property(self):
        board = Board(12)
        al = Player("Al")
        al.move_player(5, board)
        al.buy_property(board)
        fred = Player("Fred")
        fred_money = fred.money
        al_money = al.money
        fred.move_player(5, board)
        fred.pay_rent(al, board)
        rent = board.squares[5].price * 0.1
        self.assertEqual(fred.money, fred_money - rent)
        self.assertEqual(al.money, al_money + rent)




            
if __name__ == '__main__':
    unittest.main()
