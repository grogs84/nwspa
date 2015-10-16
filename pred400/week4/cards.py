

class Card(object):

	def __init__(self, suit, value, color):
		self.suit = suit
		self.value = value
		self.color = color

	def __repr__(self):
		return 'Suit: {}\nValue: {}\nColor: {}\n'.format(self.suit, self.value, self.color)

class Deck(object):

	def __init__(self):
		self.cards = self.build_deck()
		self.selected_cards = []
		self.selected_cards_count = len(self.selected_cards)

	def build_deck(self):
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		suits = {'spade':'black','heart':'red','diamonds':'red','club':'black'}
		deck = []
		for suit in suits:
			for value in values:
				card = Card(suit,value,suits[suit])
				deck.append(card)
		return deck

	def draw_wo_replacement(self):
		c = self.cards.pop()
		self.selected_cards.append(c)

	def card_count(self):
		return len(self.cards)



if __name__ == '__main__':

	d = build_deck()
	
	for c in d:
		print c