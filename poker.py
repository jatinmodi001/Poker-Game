def straight(ranks):
	if len(set(ranks))==5 and (max(ranks)-min(ranks)==4):
		return True
	return False

def flush(suits):
	if len(set(suits)) == 1:
		return True
	return False

def kind(n,ranks):
	for x in ranks:
		if ranks.count(x) == n:
			return x
	return None

def two_pair(ranks):
	hicard = kind(2,ranks)
	locard = kind(2,tuple(reversed(ranks)))
	if hicard != locard :
		return (hicard,locard)
	return None

def card_ranks(hand):
	ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
	ranks.sort(reverse = True)
	return ranks

def card_suits(hand):
	suits = [s for r,s in hand]
	return suits

def poker(hand):
	return max(hand,key=hand_rank)

def hand_rank(hand):
	ranks = card_ranks(hand)
	suits = card_suits(hand)

	if straight(ranks) and flush(suits):
		return (8,max(ranks))

	elif kind(4,ranks):
		return (7,kind(4,ranks),kind(1,ranks))

	elif kind(3,ranks) and kind(2,ranks):
		return (6,kind(3,ranks),kind(2,ranks))

	elif flush(suits):
		return (5,set(suits))

	elif straight(ranks):
		return (4,set(ranks))

	elif kind(3,ranks):
		return (3,set(ranks))

	elif two_pair(ranks):
		return (2,two_pair(ranks),)

	elif kind(2,ranks):
		return (1,set(ranks))

	return (0,ranks)

if __name__ == '__main__':
#	print("Enter 5 cards")
	hand = ['6C','5C','KC','QH','JC']
	print(poker(hand))
	"""
	for x in range(5):
		hand.append(input())
	res = hand_rank(hand)
	if res[1] == 14 and res[0] == 8:
		print("Royal Flush")
	elif res[0]== 8 :
		print("Straight Flush")
	elif res[0]== 7 :
		print("Four of a Kind")
	elif res[0]== 6 :
		print("Full House")
	elif res[0]== 5 :
		print("Flush")
	elif res[0]== 4 :
		print("Straight")
	elif res[0]== 3 :
		print("Three of a kind")
	elif res[0]==2 :
		print("Two pair")
	elif res[0]==1 :
		print("One pair")
	else:
		print("High Card")
	"""
