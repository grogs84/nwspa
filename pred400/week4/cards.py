import random

class Card(object):

	def __init__(self, suit, value, color):
		self.suit = suit
		self.value = value
		self.color = color
		

	def __repr__(self):
		return 'Suit: {}\nValue: {}\nColor: {}\n'.format(self.suit, self.value, self.color)

class Deck(object):

	def __init__(self):
		self.values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
		self.cards = self.build_deck()
		self.selected_cards = []
		self.selected_cards_count = len(self.selected_cards)

	def build_deck(self):

		suits_color = {'spade':'black', 'club':'black', 'diamonds':'red','heart':'red'}
		deck = []
		for value in self.values:
			for suit in suits_color:
				card = Card(suit,value,suits_color[suit])
				deck.append(card)
		return deck

	def draw(self,replace=True):
		if replace == True:
			random_index = random.randrange(0, self.count())
			return self.cards[random_index]
		else:
			random_index = random.randrange(0, self.count())
			c = self.cards.pop(random_index)
			self.selected_cards.append(c)
			return c

	def draw_wo_replacement(self):
		c = self.cards.pop()
		self.selected_cards.append(c)

	def count(self):
		return len(self.cards)

	def count_selected(self):
		return len(self.selected_cards)

	def prob_higher(self, card):
		count = sum([self.card_rank(card) < self.card_rank(c) for c in self.cards])
		return float(count)/self.count()

	def prob_lower_or_equal(self,card):
		return 1.0 - self.prob_higher(card)

	def card_rank(self, card):
		return self.values.index(card.value)


if __name__ == '__main__':
	deck = Deck()

	print '\n'
	print 'cards in deck: {}'.format(deck.count())
	print '\n'
	print '----draw a random card with replacement---'
	c = deck.draw()
	print c
	print 'cards in deck: {}'.format(deck.count())
	print '\n'
	print '----draw a random card with out replacement---'
	c = deck.draw(replace=False)
	print c
	print 'cards in deck: {}'.format(deck.count())
	print 'cards selected: {}'.format(deck.count_selected())

