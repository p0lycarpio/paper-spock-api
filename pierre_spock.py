import random

def game(choix):
    roles = {0: "pierre", 1: "papier", 2: "ciseaux", 3: "lezard", 4: "spock"}
    choix = int(choix)

# L'ordi choisit un nombre random sauf celui du joueur.
    if(0 <= choix and choix < 5):
        ordi = random.choice([ele for ele in roles.keys() if ele != choix])

        true_table = ([
        # 0=lose, 1=win, 2=draw.

            [2,0,1,1,0], #Rock
            [1,2,0,0,1], #Paper          
            [0,1,2,1,0], #Scissors
            [0,1,0,2,1], #Lizard
            [1,0,1,0,2] #Spock
        ])

# Parcourir la true table en fonction du nb joueur et ordi
        process = true_table[choix][ordi]

        if process == 0:
            return({"result" : "Vous avez perdu",
            "jeu":{
                "ordi": roles[ordi],
                "joueur" : roles[choix]}
            })
        elif process == 1:
            return({"result" : "Vous avez gagné",
            "jeu":{
                "ordi": roles[ordi],
                "joueur" : roles[choix]}
            })
        else:
            return({2 : "Égalité"})
