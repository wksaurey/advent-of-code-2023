from util import read_stripped_lines
import time

FIVE = 0
FOUR = 1
FULL = 2
THREE = 3
TWO = 4
ONE = 5
HIGH = 6

HANDSIZE = 5

def main():
    starttime = time.time()
    rounds = read_stripped_lines('input/day7.text')
    hands = []
    for round in rounds:
        hands.append(Hand(round))
    print(f'Unsorted: {list(map(str, hands))}')
    bubbleSort(hands)
    print(f'Sorted: {list(map(str, hands))}\n')
    score = calculateScore(hands)
    print(f'Score: {score}')
    endtime = time.time()
    print(f'Run in {endtime-starttime} seconds\n')

def calculateScore(hands):
    score = 0
    for index, hand in enumerate(hands):
        score += hand.bet * (index+1)
    return score

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j].compare(arr[j+1]) == 1:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class Hand:
    def __init__(self, round):
        round = round.split()
        self.hand = round[0]
        self.bet = int(round[1])
        self.type = self.getType()
    
    def __str__(self):
        return str(self.hand) + ' ' + str(self.bet)

    # -1 if other > self, 0 if =, 1 if self > other
    def compare(self, other):
        # the smaller the type, the better
        if self.type < other.type:
            return 1
        if self.type > other.type:
            return -1
        for index in range(HANDSIZE):
            selfCard = self.cardToInt(self.hand[index])
            otherCard = self.cardToInt(other.hand[index])
            if otherCard == None:
                print('Something is wrong...')
            if selfCard < otherCard:
                return -1
            if selfCard > otherCard:
                return 1
        else:
            print(f'Hands {self.hand} and {other.hand} are equal')
            return 0

    def cardToInt(self, card):
        if card.isdigit():
            return int(card)
        if card == 'A':
            return 14
        if card == 'K':
            return 13
        if card == 'Q':
            return 12
        if card == 'J':
            return 11
        if card == 'T':
            return 10
        else:
            print(f'The card {card} is unknown')
    
    def getType(self):
        quantity = self.orderCards()
        if 5 in quantity:
            return FIVE
        if 4 in quantity:
            return FOUR
        if 3 in quantity and 2 in quantity:
            return FULL
        if 3 in quantity:
            return THREE
        if quantity.count(2) == 2:
            return TWO
        if quantity.count(2) == 1:
            return ONE
        else:
            return HIGH
        
    def orderCards(self):
        cards = []
        quantity = []
        for card in self.hand:
            if len(cards) == 0:
                cards.append(card)
                quantity.append(1)
                continue
            match = False
            for index, type in enumerate(cards):
                if type == card:
                    quantity[index] += 1
                    match = True
                    break
            if not match:
                cards.append(card)
                quantity.append(1)
                continue
        return quantity


            


main()