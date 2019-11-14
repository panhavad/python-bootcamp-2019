"""
	2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce) 
	S(pades), H(earts), D(iamonds), C(lubs)
"""

P1_WIN = "Player 1 WIN"
P2_WIN = "Player 2 WIN"
TIE = "Tie"

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
    spacial_ace = [2, 3, 4, 5, 14]
    card_value_list, card_index = sorted(card_value_list), 0

    while (card_index+1 < len(card_value_list)):
        if 	card_value_list == spacial_ace:
            card_value_list[-1] = 1
            return [max(card_value_list), True]
        elif (card_value_list[card_index] + 1 == card_value_list[card_index + 1]):
            card_index += 1
            continue
        else:
            return [0, False]
    return [max(card_value_list), True]

def is_pair(card_value_list):
    res = repeat_checker(card_value_list, 2)
    if res[-1]:
        return [res[0], True]
    else:
        return [0, False]

def is_three_same(card_value_list):
    res = repeat_checker(card_value_list, 3)
    if res[-1]:
        return [res[0], True]
    else:
        return [0, False]
	
def is_four_same(card_value_list):
    res = repeat_checker(card_value_list, 4)
    if res[-1]:
        return [res[0], True]
    else:
        return [0, False]

def is_two_pair(card_value_list):
	card_value_set = set(card_value_list)
	pair_flag = 0
	
	for card_value in card_value_set:
		occurences_counter = card_value_list.count(card_value)
		if occurences_counter is 2:
			pair_flag += 1
			if pair_flag is 2:
				return [card_value, True]
			
			else:
				continue
		
		else:
			continue
	
	return [0, False]

def is_royal(card_value_list):
	if is_straight(card_value_list)[-1] and min(card_value_list) is 10:
		return True
	else:
		return False

#check the repeating card
def repeat_checker(card_value_list, occurences):
    card_value_set = set(card_value_list)
    for card_value in card_value_set:
        occurences_counter = card_value_list.count(card_value)
        if occurences_counter is occurences:
            return [card_value, True]
        else:
            continue
	
    return [0, False]

def separator(simple_hand):
	card_value_list, card_suit_list = list(), list()

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
	return sorted(card_value_list), sorted(card_suit_list)


def poker_judge(simple_hand):
    card_value_list, card_suit_list = separator(simple_hand)

    if is_pair(card_value_list)[-1]:
        if is_three_same(card_value_list)[-1]:
            res = is_three_same(card_value_list)[0]
            return [res, 70]#Full House
		
        elif is_two_pair(card_value_list)[-1]:
            res = is_two_pair(card_value_list)[0]
            return [res, 30]#Two pair
		
        else:
            res = is_pair(card_value_list)[0]
            return [res, 20]#One pair
	
    elif is_three_same(card_value_list)[-1]:
        res = is_three_same(card_value_list)[0]
        return [res, 40]#Three of a Kind
	
    elif is_four_same(card_value_list)[-1]:
        res = is_four_same(card_value_list)[0]
        return [res, 80]#Four of a Kind"
	
    elif is_straight(card_value_list)[-1]:
        if is_royal(card_value_list):
            if is_flush(card_suit_list):
                res = max(card_value_list)
                return [res, 100]#Royal Flush
		
        elif is_flush(card_suit_list):
            res = is_straight(card_value_list)[0]
            return [res, 90]#Straight Flush
		
        else:
            res = is_straight(card_value_list)[0]
            return [res, 50]#Staright
    elif is_flush(card_suit_list):
        res = max(card_value_list)
        return [res, 60]#Flush
	
    else:
        res = max(card_value_list)
        return [res, 10]#No pair

def elem_check(simple_p1_hand, simple_p2_hand):
    card_value_list_p1, card_value_list_p2 = separator(simple_p1_hand)[0], separator(simple_p2_hand)[0]
    
    return sum(card_value_list_p1), sum(card_value_list_p2)

def poker_real(player_one, player_two):
    p1_score, p2_score = poker_judge(player_one), poker_judge(player_two)
    score, card_value = -1, 0

    if p1_score[score] == p2_score[score]:
        if p1_score[card_value] > p2_score[card_value]:
            return P1_WIN
        elif p1_score[card_value] < p2_score[card_value]:
            return P2_WIN
        elif p1_score[card_value] == p2_score[card_value]:
            p1_score, p2_score = elem_check(player_one, player_two)
            if p1_score > p2_score:
                return P1_WIN
            elif p1_score < p2_score:
                return P2_WIN
            else:
                return TIE
    elif p1_score[score] > p2_score[score]:
        return P1_WIN
    else:
        return P2_WIN