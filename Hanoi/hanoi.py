# Definizione funzione per la risoluzione
# In questo caso il parametro lc costituisce il piolo di partenza, la quello finale, lb il centrale
def hanoi(la, lb, lc):
    # Nell'esempio proposto i pioli e i dischi sono già inizializzati secondo le specifiche di questa funzione
    # Per rendere hanoi più universalmente applicabile propongo una serie di manovre di riconfigurazione
    # delle liste in ingresso al fine di adattarle allo standard
    # Eventuali elementi non corrispondenti a interi positivi verranno rimossi
    [lc.append(x) for x in la]
    la.clear()
    [lc.append(x) for x in lb]
    lb.clear()
    onlyuniquesandpositives = [] 
    [onlyuniquesandpositives.append(x) for x in lc if x not in onlyuniquesandpositives and x > 0]
    lc = onlyuniquesandpositives
    ready = True
    if lc.__len__() < 3:
        print('Impossibile eseguire il gioco:\nCarenza di dischi')
        ready = False
    if ready:
        lc.sort()
        lc.reverse()
        # Configurazione originale di lc
        olc = []
        [olc.append(x) for x in lc]
        # Registrazione ultima mossa per evitare di procedere a ritroso
        # E' sufficiente tenere conto del piolo sul quale è stato mosso il disco
        # Allo spostamento di un disco possono infatti sempre conseguire:
        #    lo spostamento inverso dello stesso disco (da evitare)
        #    lo spostamento di uno e uno soltanto altro disco
        # E' una volta spostato un disco diverso che viene riammesso lo spostamento inverso
        lastl = ''
        # Lo svolgimento del gioco sarà salvato di mossa in mossa in una lista
        # contenente ogni piolo e l'ultima mossa effettuata
        moveresult = [la, lb, lc, lastl]
        movescounter = 0
        #print(f'Mossa {movescounter}\na: {moveresult[0]}\nb: {moveresult[1]}\nc: {moveresult[2]}')
        draw_mov(moveresult[0], moveresult[1], moveresult[2], movescounter)
        while moveresult[0] != olc:
            if movescounter == 0:
                moveresult = mov_from_lc(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                movescounter += 1
                continue
            match moveresult[3]:
                case 'a':
                    moveresult = mov_from_lc(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                    if moveresult[3] != 'b':
                        moveresult = mov_from_lb(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                case 'b':
                    moveresult = mov_from_lc(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                    if moveresult[3] != 'a':
                        moveresult = mov_from_la(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                case 'c':
                    moveresult = mov_from_lb(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
                    if moveresult[3] != 'a':
                        moveresult = mov_from_la(moveresult[0], moveresult[1], moveresult[2], moveresult[3])
            movescounter += 1
            #print(f'Mossa {movescounter}\na: {moveresult[0]}\nb: {moveresult[1]}\nc: {moveresult[2]}')
            draw_mov(moveresult[0], moveresult[1], moveresult[2], movescounter)
                         
# Ogni movimento è atto a far raggiungere a un disco il piolo disponibile più distante
# rispetto a quello da cui muove     
# Movimenti da lc  
def mov_from_lc(la, lb, lc, lastl):
    if la.__len__() == 0 or (lc.__len__() != 0 and lc[len(lc) - 1] < la[len(la) - 1]):
        la.append(lc[len(lc) - 1])
        lc.pop()
        lastl = 'a'
    elif lb.__len__() == 0 or (lc.__len__() != 0 and lc[len(lc) - 1] < lb[len(lb) - 1]):
        if lc.__len__() != 0:
            lb.append(lc[len(lc) - 1])
            lc.pop()
            lastl = 'b'
    return [la, lb, lc, lastl]
        
# Movimenti da lb        
def mov_from_lb(la, lb, lc, lastl):
    if la.__len__() == 0 or (lb.__len__() != 0 and lb[len(lb) - 1] < la[len(la) - 1]):
        la.append(lb[len(lb) - 1])
        lb.pop()
        lastl = 'a'
    elif lc.__len__() == 0 or (lb.__len__() != 0 and lb[len(lb) - 1] < lc[len(lc) - 1]):
        if lb.__len__() != 0:
            lc.append(lb[len(lb) - 1])
            lb.pop()
            lastl = 'c'
    return [la, lb, lc, lastl]
        
# Movimenti da la
def mov_from_la(la, lb, lc, lastl):
    if lc.__len__() == 0 or la[len(la) - 1] < lc[len(lc) - 1]:
            lc.append(la[len(la) - 1])
            la.pop()
            lastl = 'c'
    elif lb.__len__() == 0 or la[len(la) - 1] < lb[len(lb) - 1]:
        lb.append(la[len(la) - 1])
        la.pop()
        lastl = 'b'
    return [la, lb, lc, lastl]

# Definizione funzione per la stampa di dischi e pioli
def draw_mov(la, lb, lc, movescounter):
    # Nell'esempio corrente a ogni disco corrisponde un numero n tale che 1 <= n <= quantità dischi
    # impostata dall'utente
    # Siccome però hanoi() potrebbe avere successo anche nel caso dell'assegnazione
    # di numeri naturali non per forza consecutivi, purchè sempre unici nella relativa lista,
    # predispongo una funzione di disegno in grado di proporzionare le misure dei pioli 
    # a prescindere
    # Si rende pertanto necessario individuare il disco di maggiori dimensioni, 
    # al fine di stabilire la distanza minima tra i pioli, e al contempo
    # di calcolare comunque la quantità di dischi, per fissare l'altezza sempre dei pioli 
    discomax = 0
    dischi = 0
    for x in la:
        if x > discomax:
            discomax = x
        dischi += 1
    for x in lb:
        if x > discomax:
            discomax = x
        dischi += 1
    for x in lc:
        if x > discomax:
            discomax = x
        dischi += 1
        
    # lunghezza = 6 * discomax + 4
    altezza = dischi + 1

    print(f'Mossa {movescounter}')
    # Stampa riga per riga
    for x in reversed(range(0, altezza)):
        # Fondamenta
        if x == 0:
            for y in range(0, 3):
                for z in range(0, discomax + 1):
                    print('___', end='')
                print('|', end='')
                for z in range(0, discomax):
                    print('___', end='')
            print('___')
            print('')
            
            # Indici pioli
            for y in range(0, 3):
                for z in range(0, discomax + 1):
                    print('   ', end='')
                match y:
                    case 0:
                        print('A', end='')
                    case 1:
                        print('B', end='')
                    case 2:
                        print('C', end='')
                for z in range(0, discomax):
                    print('   ', end='')
            print('')
        else:
            for y in range(0, 3):
                # Ogni piano di ogni piolo corrisponde a un valore di 1 sottratto a x
                match y:
                    case 0:
                        # Se presente a tale livello un disco sullo specifico piolo
                        # non verrà lanciata l'eccezione per "Index out of range"
                        try:
                            discoposizioneattuale = la[x-1]
                            for z in range(0, discomax + 1 - discoposizioneattuale):
                                print('   ', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            print('|', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            for z in range(0, discomax - discoposizioneattuale):
                                print('   ', end='')
                        # Altrimenti si stamperà unicamente il piolo
                        except:
                            for z in range(0, discomax + 1):
                                print('   ', end='')
                            print('|', end='')
                            for z in range(0, discomax):
                                print('   ', end='')
                    case 1:
                        try:
                            discoposizioneattuale = lb[x-1]
                            for z in range(0, discomax + 1 - discoposizioneattuale):
                                print('   ', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            print('|', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            for z in range(0, discomax - discoposizioneattuale):
                                print('   ', end='')
                        except:
                            for z in range(0, discomax + 1):
                                print('   ', end='')
                            print('|', end='')
                            for z in range(0, discomax):
                                print('   ', end='')
                    case 2:
                        try:
                            discoposizioneattuale = lc[x-1]
                            for z in range(0, discomax + 1 - discoposizioneattuale):
                                print('   ', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            print('|', end='')
                            for z in range(0, discoposizioneattuale):
                                print('___', end='')
                            for z in range(0, discomax - discoposizioneattuale):
                                print('   ', end='')
                        except:
                            for z in range(0, discomax + 1):
                                print('   ', end='')
                            print('|', end='')
                            for z in range(0, discomax):
                                print('   ', end='')
                
            print('   ')