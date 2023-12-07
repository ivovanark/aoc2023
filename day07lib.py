import sqlite3

def start_up():
    con = sqlite3.connect('day7.sqlite')
    con.execute('DROP TABLE IF EXISTS day07')
    con.commit()
    con.execute('CREATE TABLE IF NOT EXISTS day07 (' \
	        'card varchar(5) not null,' \
            'bid int not null,' \
            'weight int null,'  \
            'weight1 int null,'\
            'weight2 int null,'\
            'weight3 int null,'\
            'weight4 int null,'\
            'weight5 int null)')
    con.commit()
    con.execute('DELETE FROM day07')
    con.commit()
    con.execute('DROP TABLE IF EXISTS day07v2')
    con.commit()
    con.execute('CREATE TABLE IF NOT EXISTS day07v2 (' \
	        'card varchar(5) not null,' \
            'bid int not null,' \
            'weight int null,'  \
            'weight1 int null,'\
            'weight2 int null,'\
            'weight3 int null,'\
            'weight4 int null,'\
            'weight5 int null)')
    con.commit()
    con.execute('DELETE FROM day07v2')
    con.commit()
    
    con.close()

def register_card(card,bid,w,w1,w2,w3,w4,w5):
    con = sqlite3.connect('day7.sqlite')
    sql = 'INSERT INTO day07(card,bid,weight,weight1,weight2,weight3,weight4,weight5) values (:card, :bid, :w, :w1, :w2, :w3, :w4, :w5)'
    args = {'card':card,'bid':bid,'w':w,'w1':w1,'w2':w2,'w3':w3,'w4':w4,'w5':w5}
    con.execute(sql,args)
    con.commit()
    con.close()    

def register_card_v2(card,bid,w,w1,w2,w3,w4,w5):
    con = sqlite3.connect('day7.sqlite')
    sql = 'INSERT INTO day07v2(card,bid,weight,weight1,weight2,weight3,weight4,weight5) values (:card, :bid, :w, :w1, :w2, :w3, :w4, :w5)'
    args = {'card':card,'bid':bid,'w':w,'w1':w1,'w2':w2,'w3':w3,'w4':w4,'w5':w5}
    con.execute(sql,args)
    con.commit()
    con.close()    

def get_single_card_score(s,v):
    # volgorde: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    if s == 'A':
        return 1
    if s == 'K':
        return 2
    if s == 'Q':
        return 3
    if s == 'J' and v == 1:
        return 4
    if s == 'J' and v != 1:
        return 98
    if s == 'T':
        return 5
    if s == '9':
        return 6
    if s == '8':
        return 7
    if s == '7':
        return 8
    if s =='6':
        return 9
    if s == '5':
        return 10
    if s == '4':
        return 11
    if s == '3':
        return 12
    if s == '2':
        return 13
    
    return 99

def rate_hand(card, p = False):
    pics = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    hand = []
    size_card = len(card)
    i = 0
    for p in pics:
        hand.append(card.count(pics[i]))
        i = i+1
    # print(card,hand)
    if hand.count(5) == 1:
        if p == True: print('Card ',card,'has Five of a Kind')
        return 0
    if hand.count(4) == 1:
        if p == True: print('Card ',card,'has Four of a Kind')
        return 1
    if hand.count(3) == 1 and hand.count(2) == 1:
        if p == True: print('Card ',card,'Full House')
        return 2
    if hand.count(3) == 1:
        if p == True: print('Card ',card,'Three of a kind')
        return 3
    if hand.count(2) == 2:
        if p == True: print('Card ',card,'Two Pairs')
        return 4
    if hand.count(2) == 1:
        if p == True: print('Card ',card,'One Pair')
        return 5
    return 6

def rate_all(p = False):
    con = sqlite3.connect('day7.sqlite')
    sql = 'SELECT bid, card from day07 order by weight, weight1, weight2, weight3, weight4, weight5'
    res = con.execute(sql).fetchall()
    
    score = 0
    weight = len(res)

    for row in res:
        
        score = score + int(row[0]) * weight
        if p == True: print(row[1],row[0],weight,score)
        weight = weight - 1

    con.close()

    return score

def rate_hand_2(card, p = False):
    pics = ['A','K','Q','T','9','8','7','6','5','4','3','2']
    hand = []
    size_card = len(card)
    i = 0
    for p in pics:
        hand.append(card.count(pics[i]))
        i = i+1
    count_j = 0
    count_j = card.count('J')
    # five of a kind
    times_5 = hand.count(5)
    times_4 = hand.count(4)
    times_3 = hand.count(3)
    times_2 = hand.count(2)
    times_1 = hand.count(1)

    if times_5 == 1 or (times_4 == 1 and count_j == 1) or (times_3 == 1 and count_j == 2) or (times_2 == 1 and count_j == 3) or count_j >= 4:
        if p == True: print(card,count_j,'Five of a kind')
        return 0
    if times_4 == 1 or (times_3 == 1 and count_j == 1) or (times_2 == 1 and count_j >= 2) or count_j >= 3:
        if p == True: print(card,count_j,'Four of a kind')
        return 1
    if (times_3 == 1 and count_j > 1) or (times_2 == 2 and count_j == 1 ) or (times_2 == 1 and count_j >= 2) or (times_3 == 1 and times_2 == 1):
        if p == True: print(card,count_j,'Full house')
        return 2
    if (times_2 == 1 and count_j >= 1) or count_j >= 2 or times_3 == 1:
        if p == True: print(card,count_j,'Three of a kind')
        return 3
    # 2 pairs
    if times_2 == 2 or (count_j >= 1 and times_2 == 1) or count_j >= 2:
        if p == True: print(card,count_j,'Two pairs')
        return 4
    # 1 pair
    if times_2 == 1 or count_j >= 1:
        if p == True: print(card,count_j,'One pair')
        return 5
    return 6

def rate_all_v2(p = False):
    con = sqlite3.connect('day7.sqlite')
    sql = 'SELECT bid, card, weight from day07v2 order by weight, weight1, weight2, weight3, weight4, weight5'
    res = con.execute(sql).fetchall()
    
    score = 0
    weight = len(res)

    for row in res:
        match row[2]:
            case 0: x = 'Five of a kind'
            case 1: x = 'Four of a kind'
            case 2: x = 'Full House'
            case 3: x = 'Three of a kind'
            case 4: x = 'Two pairs'
            case 5: x = 'One pair'
            case _: x = '-'
       
        score = score + int(row[0]) * weight
        if p == True: print(row[1],row[0],x,weight,score)
        weight = weight - 1

    con.close()

    return score