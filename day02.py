txt = open('day-02-input.txt','r')
som = 0

for txtline in txt:
    txtline = txtline.replace('\n','')
    txtline_elements = txtline.split(':')
    game_id = txtline_elements[0].split(' ')[1]
    games = txtline_elements[1].split(';')
    line_result = True # dit is het resultaat van alle games in 1 line
    for game in games:
        game_result = True
        result_list = game.split(',')
        for result in result_list:
            result = result.split(' ')
            clr = result[2].replace('\n','') # result[0] is een spatie 
            qty = int(result[1])
            if (clr == 'red' and qty > 12) or (clr == 'blue' and qty > 14) or (clr == 'green' and qty > 13 and qty > 0):
                game_result = False
                # print(game_id, result,'is ongeldig.')
                break
        if game_result == False:
            # dan is alles niet goed:
            line_result = False
            break
    if line_result == True:
        som = som + int(game_id)
        
print('Totaal van valide game-ID\'s is ', str(som))

# voor vraag 2 opnieuw door de dataset heen:
txt.seek(0)
pwr = 0
for txtline in txt:
    txtline = txtline.replace('\n','')
    txtline_elements = txtline.split(':')
    game_id = txtline_elements[0].split(' ')[1]
    games = txtline_elements[1].split(';')
    max_red_found = 1
    max_blue_found = 1
    max_green_found = 1
        
    for game in games:
        result_list = game.split(',')
        for result in result_list:
            result = result.split(' ')
            clr = result[2].replace('\n','') # result[0] is een spatie 
            qty = int(result[1])
            if clr == 'red' and qty > max_red_found:
                max_red_found = qty
            if clr == 'blue' and qty > max_blue_found:
                max_blue_found = qty
            if clr == 'green' and qty > max_green_found:
                max_green_found = qty
    pwr = pwr + (max_blue_found * max_green_found * max_red_found)

print('Power:', str(pwr))    