# Score categories
# Change the values as you see fit
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "4_of_a_kind"
# If the straights are both 30 the tests fail. This solution is ugly and buggy!
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = "straight"
CHOICE = "choice"


def score(dice, category):

    setd = set(dice)
    most_of = max(dice, key=dice.count)
    num_of_most = dice.count(most_of)
    
    if category in (ONES, TWOS, THREES, FOURS,FIVES,SIXES):
        return dice.count(category) * category

    elif category == YACHT and len(set(dice)) == 1:
        return category

    elif category == FOUR_OF_A_KIND and num_of_most >= 4:
        return 4 * most_of

    elif category == LITTLE_STRAIGHT and setd == set([1, 2, 3, 4, 5]):
        return category

    elif category == BIG_STRAIGHT and setd == set([2, 3, 4, 5, 6]):
        return 30

    elif category == FULL_HOUSE and len(set(dice)) == 2 and num_of_most == 3:
        return sum(dice)

    elif category == CHOICE:
        return sum(dice)

    else:
        return 0
