'''
Dal punto di vista logico la struttura fisica può essere sintetizzata in tre liste (i pioli).
Da un piolo all'altro si sposteranno secondo le regole del gioco n dischi
interpretati da n numeri naturali consecutivi.
All'utente verrà permesso di indicare una quantità non inferiore a 3 di dischi.
Pioli e dischi verranno stampati in console a ogni passaggio risolutivo.
'''
import hanoi
# Quantità dischi
dischi = input("Quanti dischi ?\n")

# Verifica dell'appartenenza a N dell'input
while True:
    try:
        dischi = int(dischi)
        while(dischi < 3):
            dischi = input("Necessariamente maggiore o uguale a 3\n")
            dischi = int(dischi)
        break
    except:
        dischi = input("Necessariamente intero\n")
        
# Inizializzazione dei pioli
pa = []
pb = []
pc = []

# Assegnazione dischi
for x in range(1, dischi + 1):
    pc.append(x)

# Inversione dell'ordine dei dischi
pc.reverse()

hanoi.hanoi(pa, pb, pc)