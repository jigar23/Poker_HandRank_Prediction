from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

# Rank is 2-14 representing 2-A, while suit is 1-4 representing spades, hearts, diamonds, clubs
# aceOfSpades = Card(14, 1)
# twoOfDiamonds = Card(2, 3)

hole = [Card(10, 2), Card(11, 2)]
board = [Card(12, 2), Card(13, 1), Card(14, 2),Card(4, 1)]
score = HandEvaluator.evaluate_hand(hole, board)
print(score)