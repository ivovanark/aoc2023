txt = open('day-01-input.txt','r')
som = 0

def nummer_uit_string_halen(txt_in):
    # haal 1e numerieke karakter uit een string en laatste numerieke uit een string, en voeg die samen tot een getal
    # dus '1' en '8' wordt 18
    j = len(t) -1
    i = 0
    first = 0
    last = 0
    while i <= j:
        if(txt_in[i] in ('0123456789')):
            first = txt_in[i]
            break
        i = i+1
    while j >= 0:
        if(txt_in[j] in ('0123456789')):
            last = (txt_in[j])
            break
        j = j-1
    return int(first + last)

# dag 1, vraag 1:
for t in txt:
    som = som + nummer_uit_string_halen(t)
print('Totaal vraag 1: ' , som)    

# dag 1, vraag 2: 
# variabelen resetten:
som = 0

# terug naar begin file
txt.seek(0)

for t in txt:
    # een line kan zowel eighTwo bevatten en dat gaat niet lekker want daat moet 28 worden
    # dus we kunnen niet zomaar de string vervangen want dan wordt het eigh2
    # van dik hout zaagt men plaken:
    woorden = ['one','two','three','four','five','six','seven','eight','nine']
    getallen = [1,2,3,4,5,6,7,8,9]
    a = 0
    while a < 9:
        t = t.replace(woorden[a], woorden[a] + str(getallen[a]) + woorden[a])
        a = a+1
        
    som = som + nummer_uit_string_halen(t)
    
print('Totaal vraag 2: ' , som)
