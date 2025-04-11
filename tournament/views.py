
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


def validate_data(data,datatype):

    if datatype == str:
        return data.isdigit() is False
    elif datatype == int:
        return data.isdigit() is True
    elif datatype == date:
        pass

    raise Exception("Data type not handled yet!")

def input_with_validator(prompt, data_type):
    # prompt = "What's the name of the tournament ?
    # 

    data_is_valid = False

    while data_is_valid == False:
        text = input(prompt)
        data_is_valid = validate_data(text, data_type)
    
    return text

     
def get_tournament_infos():
        tournament_infos = {
                    "name" : input_with_validator("What's the name of the tournament ?  ", str),
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

# Nouvelle fonction pour afficher les joueurs et récupérer les choix
def select_players_for_tournament_view(players):
    print("\n--- Sélection des joueurs ---")
    for idx, player in enumerate(players, 1):
        print(f"{idx} - {player['name']} {player['firstname']} -- ID: {player['id']}.")
    
    choix = input("Entrez les numéros des joueurs (ex: 1,3,5) : ")
    return [int(num.strip()) for num in choix.split(',')]
            
def set_scores_views(match):
      while True:
        try:
            score1 = float(input(f"Score pour {match.joueur1} (0, 0.5, 1) : "))
            if score1 not in {0, 0.5, 1}:
                raise ValueError
            return score1
        except ValueError:
            print("Erreur : Entrez uniquement 0, 0.5 ou 1")

def display_debrief(debrief_data):
    """Affiche le debrief à partir des données brutes."""
    print("\n=== DEBRIEF FINAL ===")
    
    # Classement
    print("\nClassement Final :")
    for idx, player in enumerate(debrief_data["ranking"], 1):
        print(f"{idx}. {player.name} {player.firstname} - {player.score} pts")
    
    # Détails des rounds
    print("\nDétails par Round :")
    for round in debrief_data["rounds"]:
        print(f"\n  Round {round.nom} :")
        for match in round.match_list:
            result = "Égalité" if match.score1 == 0.5 else \
                    f"Gagnant: {match.joueur1}" if match.score1 == 1 else \
                    f"Gagnant: {match.joueur2}"
            print(f"    {match.joueur1} vs {match.joueur2} → {result}")
        
def display_match(match_data): #Partie report, pour avoir les informations d'un tournoi et des rounds
    print(f"{match_data['joueur1']['name']} {match_data['joueur1']['firstname']} vs {match_data['joueur2']['name']} {match_data['joueur2']['firstname']}")


def display_round(round_data): #Partie report toujours.
    print(f"\n--- Round {round_data['nom']} ({round_data['dateStart']} à {round_data['dateEnd']}) ---")


def get_tournament_name(): #Utile pour la partie report
    return input("Nom du tournoi à afficher : ")

#Partie report 

# liste de tous les joueurs par ordre alphabétique ;
#  liste de tous les tournois ;
#  nom et dates d’un tournoi donné ;
#  liste des joueurs du tournoi par ordre alphabétique ;
# liste de tous les tours du tournoi et de tous les matchs du tour.
