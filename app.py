from flask import Flask,render_template
import os,random
app = Flask(__name__)
hand = []
hand1 = []
app.config['image_folder'] = os.path.join("static","images")
cards = ['A0.png','A1.png','A2.png','A3.png',
        '20.png','21.png','22.png','23.png',
        '30.png','31.png','32.png','33.png',
        '40.png','41.png','42.png','43.png',
        '50.png','51.png','52.png','53.png',
        '60.png','61.png','62.png','63.png',
        '70.png','71.png','72.png','73.png',
        '80.png','81.png','82.png','83.png',
        '90.png','91.png','92.png','93.png',
        'T0.png','T1.png','T2.png','T3.png',
        'J0.png','J1.png','J2.png','J3.png',
        'Q0.png','Q1.png','Q2.png','Q3.png',
        'K0.png','K1.png','K2.png','K3.png']


@app.route('/')
def index():
	random.shuffle(cards)
	hand_player1 = [cards[0],cards[1],cards[2],cards[3],cards[4]]
	hand_player2= [cards[5],cards[6],cards[7],cards[8],cards[9]]
	
	winner = poker(hand_player1,hand_player2)
	if(winner == hand_player2):
		str = "Congratulations! You Won The Game"
	else:
		str = "Better Luck Next Time"
	return render_template("index.html",hand1=hand_player1,hand2=hand_player2,str=str,winner=winner)

@app.route('/')
def shuffleCards():
	random.shuffle(cards)
	
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
	ranks = ['--23456789TJQKA'.index(r) for r,q,e,g,t,a in hand]
	ranks.sort(reverse = True)
	return ranks

def card_suits(hand):
	suits = [b for a,b,c,d,e,f in hand]
	return suits

def poker(hand1,hand2):
	return max(hand1,hand2,key=hand_rank)

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
		return (5,ranks)

	elif straight(ranks):
		return (4,max(ranks))

	elif kind(3,ranks):
		return (3,kind(3,ranks),ranks)

	elif two_pair(ranks):
		return (2,two_pair(ranks),ranks)

	elif kind(2,ranks):
		return (1,kind(2,ranks),ranks)

	return (0,ranks)

if __name__ == '__main__':
	app.config['DEBUG']=True
	app.run(port=8080)
	
	
	
	
