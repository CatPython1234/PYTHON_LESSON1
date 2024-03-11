import random


class Card(object):
    def __init__(self, rang, suit):
        self.rang=rang
        self.suit=suit

    def card_value(self):
        if self.rang in "TJQK":
            return 10
        else:
            return "A23456789".index(self.rang)


    def get_rang(self):
        return self.rang

    def __str__(self):
        return "%s%s" % (self.rang, self.suit)

class Hand(object):
    def __init__(self,name):
        self.name=name
        self.cards=[]

    def add_cart(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rang() == "A":
                aces += 1
        if result + aces * 10 <=21:
            result += aces * 10
        return result

    def __str__(self):
        test = "%s's держит:\n" % self.name
        for card in self.cards:
            test += str(card) + " "
        test += "\nНа руках: " + str(self.get_value())
        return test

class Deck(object):
    def __init__(self):
        ranks="23456789TJQKA"
        suits="ПБЧК"
        self.cards = [Card(r, s) for r in ranks for s in suits]
        random.shuffle(self.cards)

    def deal_card(self):
        return  self.cards.pop()


def new_game():
    d = Deck()
    player_hand = Hand("Игрок")
    dealer_hand = Hand("Дилер")
    player2_hand = Hand("Игрок2")
    player_hand.add_cart(d.deal_card())
    player_hand.add_cart(d.deal_card())
    player2_hand.add_cart(d.deal_card())
    player2_hand.add_cart(d.deal_card())
    dealer_hand.add_cart(d.deal_card())
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        ans = input("Стоп или Взять? (стоп/взять)")
        if ans == "взять":
            player_hand.add_cart(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Ты проиграл")
                in_game = False
        else:
            print("Ты вышел из игры!")
            break
    print("=" * 20)

    while player2_hand.get_value() < 19:
        ans2 = input("Стоп или Взять? (стоп/взять)")
        if ans2 == "взять":
            player2_hand.add_cart(d.deal_card())
            print(player2_hand)
            if player2_hand.get_value() > 19:
                print("Ты проиграл")
                in_game = False
        else:
            print("Ты вышел из игры!")
            break
    print("=" * 19)

    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_cart(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("Арест дилера")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("Ты победил")
        else:
            print("Выигрыш дилера")

new_game()
