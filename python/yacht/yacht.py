# Score categories
# Change the values as you see fit
YACHT = lambda di: 50 if len(set(di)) == 1 else 0
ONES = lambda di: sum(x for x in di if x ==1)
TWOS = lambda di: sum(x for x in di if x ==2)
THREES = lambda di: sum(x for x in di if x ==3)
FOURS = lambda di: sum(x for x in di if x ==4)
FIVES =lambda di: sum(x for x in di if x ==5)
SIXES =lambda di: sum(x for x in di if x ==6)
FULL_HOUSE = lambda di: sum(di) if len(set(di)) == 2 and di.count(max(di, key=di.count)) == 3 else 0
FOUR_OF_A_KIND = lambda di: 4 * max(di, key=di.count) if di.count(max(di, key=di.count)) >= 4 else 0
LITTLE_STRAIGHT = lambda di: 30 if set(di) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda di: 30 if set(di) == {6, 2, 3, 4, 5} else 0
CHOICE = lambda di: sum(di)


def score(dice, category):
     return category(dice)
