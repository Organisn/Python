'''
L'algoritmo di Euclide permette di calcolare l'MCD tra due numeri interi
mediante divisioni consecutive.
Stando a YouMath, il vantaggio risiede nella possibilità di essere all'oscuro dei numeri primi
'''
print("Algoritmo di Euclide per l\'MCD tra due interi")

# Input a
a = input("Primo\n")

# Verifica dell'appartenenza a Z
while True:
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
while True:
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

def mcd(a, b):

    print(f"Esecuzione mcd({a}, {b}) ...\n")

    # Casi con input a 0
    if a == 0 and b == 0:

        print(f"La divisione per 0 non è contemplata in Z\n")

    elif a == 0 and b != 0:

        print(f"MCD({a}, {b}) = {b}\n")
    
    elif a != 0 and b == 0:

        print(f"MCD({a}, {b}) = {a}\n")

    # Se a != 0 and b != 0
    else:

        # Registro i valori originali
        a1 = a
        
        b1 = b

        # Il procedimento in caso di input negativi resta invariato
        # Gli input in questione vengono considerati come positivi
        if a < 0:

            a = -a

        if b < 0:

            b = -b

        # Il dividendo dev'essere maggiore del divisore
        if b > a:

            c = a

            a = b

            b = c

        while b != 0:

            print(f"{a} / {b} = ", end="")

            # Divisione in Z
            # a / b = q resto r
            quoziente = 0

            # quoziente * b sempre minore o uguale ad a
            while b * quoziente <= a - b:

                quoziente += 1

            # Resto rigorosamente minore di b
            resto = a - b * quoziente

            print(f"{quoziente} resto {resto}\n")

            # Aggiornamento per la divisione seguente
            a = b

            b = resto
        
        # In Z è la divisione per 0 è impossibile

        print(f"MCD({a1}, {b1}) = +/-{a}\n")

mcd(a, b)