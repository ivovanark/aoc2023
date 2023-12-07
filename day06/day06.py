vraag1 = [[61,430],[67,1036],[75,1307],[71,1150]]

succes_lijst = []
for i in vraag1:
    j = 1
    succes = 0
    while j <= i[0]:
        wachttijd = j
        racetijd = i[0] - wachttijd
        afstand = wachttijd * racetijd
        if afstand > i[1]:
            succes = succes + 1
        j = j + 1
    # print(i, succes)
    succes_lijst.append(succes)

print('Vraag 1', succes_lijst[0] * succes_lijst[1] * succes_lijst[2] * succes_lijst[3])

vraag2 = [61677571,430103613071150]

succes = 0
j = 0
while j <= vraag2[1]:
    succes_in = succes
    wachttijd = j
    racetijd = vraag2[0] - wachttijd
    afstand = wachttijd * racetijd
    if afstand > vraag2[1]:
        succes = succes + 1
    j = j + 1
    if succes > 0 and succes == succes_in:
        # Er komt blijkbaar niks meer bij, dus stoppen met zoeken
        break
print('Vraag 2', succes)

 
