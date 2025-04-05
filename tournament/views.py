#TODO : verifier le format de L'ID
#TODO : Ajouter un joueur, avec id, nom, prenom, date de naissance
#et les passer a add player

#TODO : demander user les scores. gagnant 1 pts, perdant 0.
#match nul = 0.5
#pour un match specifique
""" Module views avec tous les prints de l'application """

def display_menu():
    print("""
            Main Menu 
          
    - 1.Create a Tournement
    - 2.Player Management
    - 3.Reports
    - 4.Quit
          
 """)
    

def get_user_choice():
    choice = input(">>>  ")
    return choice 


def display_user_management_menu():
    print(""" 
          
          Do you want to :

          1. Add a player

          2. Main Menu  """)


def another_player():
    print("""
    Do you want to add another player ? 

                1. Yes 
                2. No 
                3. Main Menu""")


def get_user_infos():
    player_infos = {
        "name" : input("What's your name ? "),
        "firstname": input("What's your first name ?  "),
        "birthdate": input("What's your birthdate ?  ")
    }
    return player_infos 


def report_menu():
        print("""
            Report Menu
              
        - 1. List of all players
        - 2. List of all tournaments
        - 3. Tournaments data 
        - 4. Access list of rounds for each tournaments and matches for each rounds.
        - 5. Main Menu
              
 """)


def menu_tournament():
     print(""" 
           Menu des tournois 
           
           1. Creer un nouveau tournoi
           2. Retour au menu principal
           
           """)
     
      
def get_tournament_infos():
        tournament_infos = {
                    "name" : input("What's the name of the tournament ?  "),
                    "description" : input("What's the tournament description ?  "),
                    "location" : input("What's the tournament location ?  "),
                    "dateStart" : input("When does the tournament start ?  "),
                    "dateEnd" : input("When does the tournament end ? "),
                    "number_of_rounds" : int(input("How many rounds ? (per default = 4)  "))}
        return tournament_infos

def get_round_infos():
     round_info = {
          "name" : input("What's the name of the round ? :  "),
          "dateStart" : input("When does it start ? :  "),
          "dateEnd" : input("When does it end ? :  ")
            }
     return round_info

def tournament_successfully_added():
        print(""" 
              
              The tournament was sucessfully created ! 
              
              Do you want to create the first round ?   

              1. Yes 
              2. No (Main Menu)
              
              """)
        
def enter_score():
        print("""
              
              Who's won the match ? 

              1. Joueur1
              2. Joueur2
              
              
              
              """)

def choose_players():
        player = input(""" 
                       
                       Enter the IDs of players who will play in this tournament, split the players by a comma : 
                       
                       """)
        return player

def display_match(match_number, total_matches, player1, player2):
    print(f"\n[MATCH {match_number}/{total_matches}]")
    print(f"1. {player1} gagne")
    print(f"2. {player2} gagne")
    print(f"3. Match nul")
            
                    
                                        
            
            
    
    ##TODO : Partie report

        ##TODO : Fonctions listes de joueurs par ordre alphabétique
                    ##TODO : print d'une liste avec un formattage alphabétique
                ##TODO : Listes des tournois
                ##TODO : print d'une liste avec tous les tournois, a voir si j'affiche les paramètres, 
                         #si j'affiche un user choice pour voir les paramètres 

            ##TODO : Partie creer un tournoi 

                ##TODO : Selon les paires les ajouter dans des matchs (match1 = Match(Joueur1, Joueur2))
                ##TODO : Prendres les victoires (input: qui a gagné ? )
                ##TODO : Trier les joueurs selon leur victoires (dictionnaire? qu'on peut stringformatter pour voir les victoires)
                         #Ou directement dans l'init du joueurs PENDANT un tournoi ? paramètre
                         #Comme ca on pourrait faire un print(Joueur1) ou un __str__ et voir son nombre de victoire
                ##TODO : Créer des matchs selon les scorings (Formattage liste -> listes vainqueurs -> classe Match sur eux)
                
                

#Partie report 

# liste de tous les joueurs par ordre alphabétique ;
#  liste de tous les tournois ;
#  nom et dates d’un tournoi donné ;
#  liste des joueurs du tournoi par ordre alphabétique ;
# liste de tous les tours du tournoi et de tous les matchs du tour.
