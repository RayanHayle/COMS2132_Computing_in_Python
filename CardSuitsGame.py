#/usr/bin/python
# -*- coding: utf-8 -*-
# Python Personal Mini-Project
import random
import sys

suits = ['♠','♣','♦','♥'] # Feel free to use these symbols to represent the different suits.
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King']

DEBUG = False

class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} {}.'.format(self.suit, self.rank)

class CardCollection(object):

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def draw_card(self):
        return self.cards.pop()

    def make_deck(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)

    def value(self):
        aces = 0
        value = 0

        for card in self.cards:
            rank = card.rank
            if rank == 'Queen' or rank == 'King' or rank == 'Jack':
                value += 10
            elif rank == 'Ace':
                aces += 1
            else:
                value += int(rank)

        if value > 10:
            value += aces
        else:
            value += 11 * (1 if aces > 0 else 0) + ((aces - 1) if aces > 0 else 0)

        if DEBUG:
            print(f'Computed value: {value}')

        return value


def main():
    deck = CardCollection()

    deck.make_deck() # initialize a fresh deck
    player_hand = CardCollection()
    dealer_hand = CardCollection()

    while True:
        draw = deck.draw_card()
        print(f'You drew: {draw}')
        player_hand.add_card(draw)
        val = player_hand.value()
        if val == 21:
            print('You win!')
            sys.exit()
        elif val > 21:
            print('You lose!')
            sys.exit()
        else:
            res = input('Do you want to draw another card? (y/n): ')
            if res == 'n':
                break
            elif not res == 'y':
                print(f'Unknown input \"{res}\" - assuming input to be \"y\"')

    while True:
        draw = deck.draw_card()
        print(f'I drew: {draw}')
        dealer_hand.add_card(draw)
        val = dealer_hand.value()

        if val == 21:
            print('You lose!')
            sys.exit()
        elif val > 21:
            print('You win!')
            sys.exit()
        elif val > 17:
            print('I chose to stay')
            break

    v1, v2 = player_hand.value(), dealer_hand.value()

    if v1 > v2:
        print('You win!')
    elif v2 > v1:
        print('You lose!')
    else:
        print('Push game')


if __name__ == "__main__":
    main()
