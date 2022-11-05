import random

def demande_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})")
        try:    
            nombre_int = int(nombre_str)
        except:
            print("vous devez rentrez un nombre ! Réessayer.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Vous devez rentrez un nombre entre {nb_min} et {nb_max}. Réessayer")
                nombre_int = 0       
    return nombre_int    
 

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 4


nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demande_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné(e) !")
    elif nombre < NOMBRE_MAGIQUE:
        print("Perdue ! Le nombre magique est plus haut")
        vies -= 1
    else:
        print("Perdue ! Le nombre est plus bas")
        vies -= 1

if vies == 0:        
    print(f"Perdue ! Vous n'avez plus de vies. Le nombre magique étais {NOMBRE_MAGIQUE}.")            
