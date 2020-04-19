
class Card:
	suit = "suit"
	rank = "rank"
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank
	def printCard(self):
		print(self.rank+"-"+self.suit, end="  ")

	def points(self):
		a = ["0", "ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
		buf = a.index(self.rank)
		if(buf > 10):
			buf = 10
		if( buf == 1):
			buf = 11
		return(buf)

class Deck:
	deck = []
	def __init__(self):
		def whichsuit(num):
			Allsuit = ["CLUB", "DIAMOND", "HEART", "SPADE"]
			buf = Allsuit[(num-1)//13]
			return(buf)

		def whichrank(num):
			buf = list(range(2, 11))
			buf1 = list(map(str, buf))	
			Allrank = ["ACE"] + buf1 + ["JACK", "QUEEN", "KING"]
			cache = Allrank[(num-1)%13]
			return(cache)

		import random
		#random.seed(4)
		seq = list(range(1, 53))
		random.shuffle(seq)
		for i in seq:
			self.deck.append(Card(whichrank(i), whichsuit(i)))

	def pop(self):
		buf = self.deck[0]
		del self.deck[0]
		return(buf)

class People:
	deck = "?"
	def __init__(self, whichdeck):
		self.deck = whichdeck.pop()
		self.deck = [self.deck] + [whichdeck.pop()]

	def withhand(self):
		for i in self.deck:
			i.printCard()
		print(" ")

def Current_Value(people):
	#people = dealer
	total, ifACE = 0, False
	for i in people.deck :
		total = total + i.points()
		if( i.points() ==11):
			ifACE = True
	if( total > 21 and ifACE):
			total = total-10
	return(total)
	
# Game start
while(True):
	# give card 
	deck = Deck()
	dealer, player = People(deck), People(deck)

	whowin = "Tie"
	endGame, breakyes = False, False
	while(True):
		buf = Current_Value(player)
		if( buf > 21):
			print("\n\nYour current value is Bust! (>21)")
			endGame = True
			whowin = "dealer"
		else:
			if( buf == 21 ):
				print("\n\nYour current value is Blackjack! (21)")
				breakyes = True
			else:
				print("\n\nYou current value is %d" % ( buf ))
		print("with the hand:", end=" ")
		player.withhand()

		if( endGame or  breakyes):
			break
		a = input("\nHit or stay? (Hit = 1, Stay = 0):")
		if(a == "1"):
			pickcard = deck.pop()
			print("You draw ", end = "")
			pickcard.printCard()
			player.deck =  player.deck + [pickcard]
		else:
			break

	firstTime, nodraw = True, True
	while(not endGame):
		buf = Current_Value(dealer)
		if(firstTime):
			print("\n\nDealer's current value is %d" % ( buf ))
			print("with the hand:", end=" ")
			dealer.withhand()
			firstTime = False

		if( buf >= 17):
			if( buf > 21 ):
				print("\n\nDealer's current value is Bust! (>21)")
				whowin = "player"
			else:
				if( buf == 21 ):
					print("\n\nDealer's current value is Blackjack! (21)")
					breakyes = True
				else:
					if (not nodraw):
						print("\n\nDealer's current value is %d" % ( buf ))
			if (not nodraw):
				print("with the hand:", end=" ")
				dealer.withhand()
			break

		if(buf < 17):
			nodraw = False
			printyes = False
			pickcard = deck.pop()
			print("\nDealer draws: ", end = "")
			pickcard.printCard()
			dealer.deck =  dealer.deck + [pickcard]

	if( whowin == "Tie"):
		pvalue, dvalue = Current_Value(player), Current_Value(dealer)
		if(pvalue > dvalue):
			whowin = "player"
		else:
			if( pvalue < dvalue):
				whowin = "dealer"
			else:
				whowin = "Tie"

	if(whowin == "Tie" ):
		print("\n*** You tied the dealer, nobody wins ***")
	if(whowin == "player" ):
		print("\n*** You beat the dealer ***")
	if(whowin == "dealer" ):
		print("\n*** Dealer wins! *** ")

	playagain = input("Want to play again? (y/n)")

	if(playagain == "n"):
		break
	else: 
		print("\n" + "*"*40)