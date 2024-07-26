'''
Input: a, b interi
Output: ab

Se a = 1 => ab = b
Se a mod 2 = 0 => ab = a/2 * 2b
Se a è dispari => ab = (a-1)b + b

Es:
	7*3 = 6*3 + 3 =  3*6 + 3 = 2*6 + 6 + 3 = 1*12 + 6 + 3 = 21
'''

print("Algoritmo di Ahmes per il prodotto di due interi")

# Input a
a = input("Primo\n")

# Verifica dell'appartenenza a Z
while(True):
    try:
        a = int(a)
        '''
        # Appartenenza a N
        while(a < 0):
            a = input("Necessariamente positivo\n")
            a = int(a)
        '''
        break
    except:
        a = input("Necessariamente intero\n")

# Input b
b = input ("Secondo\n")

# Verifica dell'appartenenza a Z
while(True):
    try:
        b = int(b)
        '''
        # Appartenenza a N
        while(b < 0):
            b = input("Necessariamente positivo\n")
            b = int(b)
        '''
        break
    except:
        b = input("Necessariamente intero\n")

# Salvo i valori originali
a1 = a

b1 = b

print(f"Esecuzione ({a}) * ({b}) ...\n")

# Caso a = 0 OR b = 0
if a == 0 or b == 0:

    print(f"({a}) * ({b}) = {a*b}")

else:

    # Il procedimento in caso di input negativi resta invariato
    # Gli input in questione vengono considerati come positivi
    if(a < 0):
        a = -a
    if(b < 0):
        b = -b

    # Lista per accogliere tutti gli addendi generati dalle moltiplicazioni consecutive
    addendi = []

    while a != 1:
        
        # Se a è pari..
        if a % 2 == 0:

            print(f"{a} * {b} ", end="")
            
            # Stampa degli addendi finora accumulati
            [print(f"+ {x} ", end="") for x in addendi]

            print(f"= {a}/2 * 2({b}) ", end="")

            [print(f"+ {x} ", end="") for x in addendi]

            print("\n")

            a /= 2

            a = int(a)

            b *= 2

        # Altrimenti..
        else:

            print(f"{a} * {b} ", end="")

            # Stampa degli addendi finora accumulati
            [print(f"+ {x} ", end="") for x in addendi]

            print(f"= ({a} - 1)({b}) ", end="")

            addendi.append(b)

            [print(f"+ {x} ", end="") for x in addendi]

            print("\n")
            
            a -= 1

    # a = 1

    print(f"{a} * {b} ", end="")
            
    # Stampa degli addendi finora accumulati
    [print(f"+ {x} ", end="") for x in addendi]

    print(f"= {b} ", end="")

    [print(f"+ {x} ", end="") for x in addendi]

    # Somma degli addendi con b
    for x in addendi:
        b += x

    print(f"= {b}\n")

    print(f"({a1}) * ({b1}) = ", end="")

    # Definizione del segno del prodotto
    if((a1 > 0 and b1 > 0) or (a1 < 0 and b1 < 0)):
        print(f"{b}\n")
    else:
        print(f"{-b}\n")