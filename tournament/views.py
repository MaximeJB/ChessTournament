#TODO : verifier le format de L'ID
#TODO : Ajouter un joueur, avec id, nom, prenom, date de naissance
#et les passer a add player

#TODO : demander user les scores. gagnant 1 pts, perdant 0.
#match nul = 0.5
#pour un match specifique

def display_menu():
    print("""
            Main Menu 
          
    - 1.Create a Tournement
    - 2.Player Management
    - 3.Reports
    - 4.Quit
          
 """)
    
def get_user_choice():
    choice = input("What's your choice ?  : ")
    return choice 

def display_user_management_menu():
    print(""" Do you want to :
          1.Add a player
          2.Remove a Player""")

def another_player():
    print("Do you want to add another player ? \n "
    "1. Yes "
    "2. No ")
    
def get_user_infos():
    player_infos = {
        "Name" : input("Quel est votre nom : "),
        "Firstname": input("What's your first name : ")
    }
    return player_infos 

    ##TODO : Partie Player Management
            ##TODO : Remplir toutes les données neccessaire pour l'ajout d'un nouveau joueur. 
            ##TODO : envoyer les résultats sur le controller 
            ##TODO : Demander si on veut ajouter un autre joueurs avant de sortir de l'ajout joeur
            ##TODO : Faire un print voici les nouveaux joueurs : et exit
            ##TODO : Faire un display pour supprimer un joueur 
            ##TODO : envoyer vers le controller vers une fonction supprimer un joueur. (.remove)
    
    ##TODO : Partie report
            ##TODO : Faire un display pour le menu de la partie report avec toutes les possibilités
            ##TODO : Récuperer l'input, l'envoyer vers le controller
            ##TODO : faire des fonctions pour chaque sous parties
                ##TODO : Fonctions listes de joueurs par ordre alphabétique
                    ##TODO : print d'une liste avec un formattage alphabétique
                ##TODO : Listes des tournois
                ##TODO : print d'une liste avec tous les tournois, a voir si j'affiche les paramètres, 
                         #si j'affiche un user choice pour voir les paramètres 

            ##TODO : Partie creer un tournoi 
                ##TODO : Verifier sur la fiche technique ce a quoi correspond un tournoi
                ##TODO : Ajouter tous les joueurs au tournoi (donc input into liste)
                ##TODO : Trier de manière random les joueurs
                ##TODO : Selon les paires les ajouter dans des matchs (match1 = Match(Joueur1, Joueur2))
                ##TODO : Prendres les victoires (input: qui a gagné ? )
                ##TODO : Trier les joueurs selon leur victoires (dictionnaire? qu'on peut stringformatter pour voir les victoires)
                         #Ou directement dans l'init du joueurs PENDANT un tournoi ? paramètre
                         #Comme ca on pourrait faire un print(Joueur1) ou un __str__ et voir son nombre de victoire
                ##TODO : Créer des matchs selon les scorings (Formattage liste -> listes vainqueurs -> classe Match sur eux)
                
                

