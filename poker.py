from random import choice

class Card:
    def __init__(self):
        self.value = [i for i in range(2, 15)]
        self.suit = ['spades', 'hearts', 'diamonds', 'clubs']

class Hand:
    def __init__(self):
        self.cards_on_hand = []
    def add_card_to_hand(self):
        while len(self.cards_on_hand) != 5:
            c = [choice(P.suit), choice(P.value)]
            if c in self.cards_on_hand:
                continue
            else:
                self.cards_on_hand.append(c)
        return self.cards_on_hand
    def check_combination_on_hand(self):
        count_values = {}
        count_suits = {'spades': 0, 'hearts': 0, 'diamonds': 0, 'clubs': 0}
        flush = 0
        straight = 0
        values = []
        for i in range(5):
            values.append(self.cards_on_hand[i][1])
        for key in count_suits:
            for i in range(5):
                if key == self.cards_on_hand[i][0]:
                    count_suits[key] += 1
        for key in count_suits:
            if count_suits[key] == 5:
                flush = 1
                break
        for i in range(5):
            count_values[self.cards_on_hand[i][1]] = 0
        for i in range(5):
            count_values[self.cards_on_hand[i][1]] += 1
        setvalues = set(values)
        if sum(values) == (min(values) + max(values)) / 2 * len(values) and values == setvalues:
            straight = 1
        values_combination = {'Pair': 0, 'Three of a Kind': 0, 'Four of a Kind': 0}
        for key in count_values:
            if count_values[key] == 2:
                values_combination['Pair'] += 1
        for key in count_values:
            if count_values[key] == 3:
                values_combination['Three of a Kind'] += 1
        for key in count_values:
            if count_values[key] == 4:
                values_combination['Four of a Kind'] += 1
        if flush == 1 and straight == 1 and min(values) == 10:
            return 'Royal Flush'
        elif flush == 1 and straight == 1:
            return 'Straight Flush'
        elif values_combination['Four of a Kind'] == 1:
            return 'Kar'
        elif values_combination['Three of a Kind'] == 1 and values_combination['Pair'] == 1:
            return 'Full House'
        elif flush == 1:
            return 'Flash'
        elif straight == 1:
            return 'Street'
        elif values_combination['Three of a Kind'] == 1:
            return 'Three'
        elif values_combination['Pair'] == 2:
            return 'Two pairs'
        elif values_combination['Pair'] == 1:
            return 'Pair'
        else:
            return 'High card'

P = Card()
player = Hand()
print(player.add_card_to_hand())
print(player.check_combination_on_hand())

#Я не умею играть в покер и учиться не сильно хочу. Правила у него дурацкие. Я их не понимаю. Код на эту штуку (50%) писал не я (честно пытался разобраться в вашем покере)