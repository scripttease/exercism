import random 

class Board():

    def __init__(self, num_squares):
        self.squares = []
        for i in range(num_squares):
            self.squares.append(Square(Square.SQUARES[i], Square.SQ_TYPE[i], Square.PRICE[i]))

    def __str__(self):
        board = ""
        for sq in range(len(self.squares)):
            board += str(self.squares[sq]) + ", "
        return board


class Square(Board):
    SQUARES = ['Go', 'One Road', 'Two Road', 'Station', 'Three Road', 'Four Road', 'Jail', 'Five Road', 'Six Road', 'Chance', 'Seven Road', 'Eight Road']
    SQ_TYPE = ['Go', 'Property', 'Property', 'Property', 'Property',
'Property', 'Chance', 'Property', 'Property', 'Jail','Property', 'Property']
    PRICE = [0,100,150,150,200,250,0,300,350,0,400,450,0]
    

    def __init__(self, name="", sq_type="", price=0, status="Vacant"):
        self.name = name
        self.sq_type = sq_type
        self.price = price
        self.status = status

    def __str__(self):
        if self.sq_type == "Property":
            return "%s, type = %s, status = %s, price = £%s" % (self.name, self.sq_type, self.status, self.price)
        else:
            return "%s, type = %s" % (self.name, self.sq_type)


class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    @property
    def roll(self):
        return random.randrange(1, (self.sides+1))

class Player:

    def __init__(self, name="", money=1000, current_position=0):
        self.name = name
        self.money = money
        self.current_position = current_position

    def move_player(self, roll, board):
        self.current_position = (self.current_position + roll) % len(board.squares)

    def current_position_print(self, board):
        sq =  board.squares[self.current_position]
        if sq.sq_type == "Property":
            return str(board.squares[self.current_position])

    def buy_property(self, board):
        sq = board.squares[self.current_position]
        is_property = sq.sq_type == "Property"
        is_vacant = sq.status == "Vacant"
        cost = sq.price
        if is_property and is_vacant:
            self.money = self.money - cost
            sq.status = "Owned by %s" % self.name
        elif is_property and not is_vacant:
            return "Property is %s" % sq.status
        else:
            return "Square cannot be bought"
    # TODO take board from all of the things...
    def pay_rent(self, property_owner, board):
        sq = board.squares[self.current_position]
        is_property = sq.sq_type == "Property"
        is_vacant = sq.status == "Vacant"
        #TODO Change this depending on if houses
        rent = sq.price * 0.1
        if is_property and not is_vacant:
            self.money = self.money - rent
            property_owner.money = property_owner.money + rent
            return "%s has paid £%s to %s" % (self.name, rent, property_owner.name)
        else:
            return "Do you want to buy this property?"
        






