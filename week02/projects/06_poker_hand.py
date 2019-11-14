"""
	2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce) 
	S(pades), H(earts), D(iamonds), C(lubs)
"""
def letter_to_num(card_value_list):
	card_num = list()
	card_letter = {
		"1"	: 1,
		"2"	: 2,
		"3"	: 3,
		"4"	: 4,
		"5"	: 5,
		"6"	: 6,
		"7"	: 7,
		"8"	: 8,
		"9"	: 9,
		"T" : 10,
		"J" : 11,
		"Q" : 12,
		"K" : 13,
		"A" : 14
	}
	
	for each_value in card_value_list:
		card_num.append(card_letter.get(each_value, "Not Found"))
	
	return card_num

def is_flush(card_suit_list):
	card_suit_set = set(card_suit_list)
	if len(card_suit_set) is 1:
		return True
	else:
		return False
		
def is_straight(card_value_list):
	card_value_list = sorted(card_value_list)
	card_index = 0
	
	while card_index+1 < len(card_value_list):	
		if card_value_list[card_index] + 1 == card_value_list[card_index + 1]:
			card_index += 1
			continue
		else:
			return False
	
	return True

def is_pair(card_value_list):
	if repeat_checker(card_value_list, 2):
		return True
	else:
		return False

def is_three_same(card_value_list):
	if repeat_checker(card_value_list, 3):
		return True
	else:
		return False
	
def is_four_same(card_value_list):
	if repeat_checker(card_value_list, 4):
		return True
	else:
		return False	

def is_two_pair(card_value_list):
	card_value_set = set(card_value_list)
	pair_flag = 0
	
	for card_value in card_value_set:
		occurences_counter = card_value_list.count(card_value)
		if occurences_counter is 2:
			pair_flag += 1
			if pair_flag is 2:
				return True
			
			else:
				continue
		
		else:
			continue
	
	return False

def is_royal(card_value_list):
	if is_straight(card_value_list) and min(card_value_list) is 10:
		return True
	else:
		return False

#check the repeating card
def repeat_checker(card_value_list, occurences):
	card_value_set = set(card_value_list)
	
	for card_value in card_value_set:
		occurences_counter = card_value_list.count(card_value)
		if occurences_counter is occurences:
			return True
		else:
			continue
	
	return False

def separator(simple_hand):
	card_value_list = list()
	card_suit_list = list()

	simple_hand = simple_hand.split(" ")

	#get value and suit
	for each_card in simple_hand:
		if len(each_card) is 2:
			card_value_list.append(each_card[0])
		
		elif len(each_card) is 3:
			card_value_list.append(each_card[0:2])
		
		card_suit_list.append(each_card[-1])

	card_value_list = letter_to_num(card_value_list)
	# print(card_value_list)
	return card_value_list, card_suit_list

def poker_judge(simple_hand):
	card_value_list, card_suit_list = separator(simple_hand)

	if is_pair(card_value_list):
		if is_three_same(card_value_list):
			return 70#Full House
		
		elif is_two_pair(card_value_list):
			return 30#Two pair
		
		else:
			return 20#One pair
	
	elif is_three_same(card_value_list):
		return 40#Three of a Kind
	
	elif is_four_same(card_value_list):
		return 80#Four of a Kind"
	
	elif is_straight(card_value_list):
		if is_royal(card_value_list):
			if is_flush(card_suit_list):
				return 100#Royal Flush
		
		elif is_flush(card_suit_list):
			return 90#Straight Flush
		
		else:
			return 50#Staright
	elif is_flush(card_suit_list):
		return 60#Flush
	
	else:
		return 10#No pair

def poker_hand(player_one, player_two):	
	p1_score = poker_judge(player_one)
	p2_score = poker_judge(player_two)

	if p1_score == p2_score:
		return "Tie"
	elif p1_score > p2_score:
		return "Player 1 WIN"
	else:
		return "Player 2 WIN"
	
print(poker_hand("2H 3H 4H 5H 6H", "KS AS TS QS JS"))
