import day07lib

the_input = 'day07input.txt'
# the_input = 'day07test.txt'

p = False # set to True to print a lot of output! 

def vraag_1(the_input, p = False):
    with open(the_input,'r') as f:
        txtlines = f.readlines()

    day07lib.start_up()

    no_of_cards = len(txtlines)

    #process a line:
    for line in txtlines:
        l = line.strip().split(' ')
        card = l[0]
        bid = l[1]
        # type kaart: 
        w = day07lib.rate_hand(card, p)
        # scores
        w1 = day07lib.get_single_card_score(card[0],1)
        w2 = day07lib.get_single_card_score(card[1],1)
        w3 = day07lib.get_single_card_score(card[2],1)
        w4 = day07lib.get_single_card_score(card[3],1)
        w5 = day07lib.get_single_card_score(card[4],1)
        day07lib.register_card(card,bid,w,w1,w2,w3,w4,w5)

    print('There are ',no_of_cards,'cards in this game!')

    print('Question 1: The total score of all hands is',day07lib.rate_all(p))

def vraag_2(the_input, p=False):
    with open(the_input,'r') as f:
        txtlines = f.readlines()

    day07lib.start_up()

    no_of_cards = len(txtlines)

    for line in txtlines:
        l = line.strip().split(' ')
        card = l[0]
        bid = l[1]
        # type kaart: 
        w = day07lib.rate_hand_2(card, p)
        # scores
        w1 = day07lib.get_single_card_score(card[0],2)
        w2 = day07lib.get_single_card_score(card[1],2)
        w3 = day07lib.get_single_card_score(card[2],2)
        w4 = day07lib.get_single_card_score(card[3],2)
        w5 = day07lib.get_single_card_score(card[4],2)
        day07lib.register_card_v2(card,bid,w,w1,w2,w3,w4,w5)

    print('Question 2: The total score of all hands is',day07lib.rate_all_v2(p))

vraag_1(the_input,p)
vraag_2(the_input,p)
