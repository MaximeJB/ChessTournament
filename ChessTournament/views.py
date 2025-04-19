
""" Module views avec tous les prints de l'application """
from typing import Any, Dict
from datetime import datetime

class Views :
    """ Classe statique regroupant toutes les méthodes de vues de l'application"""
    
     
    @staticmethod
    def display_menu() -> None:
        """ Affiche le menu principal"""

        print("""
                Main Menu 
            
        - 1.Create a Tournement
        - 2.Player Management
        - 3.Reports
        - 4.Quit
            
    """)
        
    @staticmethod
    def get_user_choice() -> str:
        """ Demande le choix de l'utilisateur et le retourne en str"""

        choice = input(">>>  ")
        return choice 

    @staticmethod
    def display_user_management_menu() -> None:
        """ Affiche le menu de gestion des joueurs."""

        print(""" 
            
            Do you want to :

            1. Add a player

            2. Main Menu  """)

    @staticmethod
    def another_player() -> None:
        """ Demande à l'utilisateur si il veut ajouter un autre joueur"""

        print("""
        Do you want to add another player ? 

                    1. Yes 
                    2. No 
                    3. Main Menu""")

    @staticmethod
    def get_user_infos() -> Dict[str,str]:
        """ Récupère un dictionnaire selon des clés Name, Firstname, et Birthdate
            pour init un joueur. 
        """

        player_infos = {
            "name" : Views.input_with_validator("What's your name ? ", str),
            "firstname": Views.input_with_validator("What's your first name ?  ", str),
            "birthdate": Views.input_with_validator("What's your birthdate ?  ", str)
        }
        return player_infos 

    @staticmethod
    def report_menu() -> None:
            """ Affiche le menu des reports """

            print("""
                Report Menu
                
            - 1. List of all players
            - 2. List of all tournaments
            - 3. Tournaments data 
            - 4. Access list of rounds for each tournaments and matches for each rounds.
            - 5. Main Menu
                
    """)

    @staticmethod
    def menu_tournament() -> None:
        """ Affiche le menu du tournoi"""

        print(""" 
            Tournament dashboard 
            
            1. Create a new tournament
            2. Back to Main Menu
            
            """)


    @staticmethod
    def input_with_validator(prompt: str, data_type: Any) -> Any:
    
        while True:
            text = input(prompt).strip()

            #Cas spécial pour les dates
            if data_type == "birthdate":
                if len(text) == 10 and text[2] == '.' and text[5] == '.':
                    try:
                        day, month, year = map(int, text.split('.'))
                        datetime(year, month, day)  
                        return text  
                    except ValueError:
                        print("Invalid date (e.g., 30.02.2000 doesn't exist)")
                else:
                    print("Expected format: DD.MM.YYYY (e.g., 05.05.2000)")
                continue

           
            try:
                if data_type == str:
                    if not text.isdigit():  # Empêche les nombres purs
                        return text
                    raise ValueError("Text expected, not number")
                
                elif data_type == int:
                    return int(text)
                
                elif data_type == float:
                    return float(text)
                    
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    @staticmethod    
    def get_tournament_infos() -> Dict[str, Any]:
            tournament_infos = {
                        "name" : Views.input_with_validator("What's the name of the tournament ?  ", str),
                        "description" : Views.input_with_validator("What's the tournament description ?  ", str),
                        "location" : Views.input_with_validator("What's the tournament location ?  ", str),
                        "dateStart" : Views.input_with_validator("When does the tournament start ?  ", str),
                        "dateEnd" : Views.input_with_validator("When does the tournament end ? ", str),
                        "number_of_rounds" : Views.input_with_validator("How many rounds ? (per default = 4)  ", int)
            }
            return tournament_infos

    @staticmethod
    def get_round_infos() -> Dict[str,str]:
        """ Récupère et retourne les informations d'un round, sert à l'init."""

        round_info = {
            "name" : Views.input_with_validator(""" 
                            What's the name of the round ? :  """, str),
            "dateStart" : Views.input_with_validator("When does it start ? :  ", str),
            "dateEnd" : Views.input_with_validator("When does it end ? :  ", str)
                }
        return round_info

    @staticmethod
    def tournament_successfully_added() -> None:
            """Confirmation de l'init et création du tournoi."""

            print(""" 
                
                The tournament was sucessfully created ! 
                
                Do you want to create the first round ?   

                1. Yes 
                2. No (Main Menu)
                
                """)




    @staticmethod
    def display_match(match_number, total_matches, player1, player2):
        """ Affiche le résultat d'un match"""

        print(f"\n[MATCH {match_number}/{total_matches}]")
        print(f"1. {player1} won")
        print(f"2. {player2} won")
        print(f"3. That's a draw !")

    @staticmethod
    def select_players_for_tournament_view(players):
        """ Sélectionne les joueurs pour le tournoi, via des numéros attribué à chacun"""

        print("\n--- Select Player ---")
        for idx, player in enumerate(players, 1):
            print(f"{idx} - {player['name']} {player['firstname']} -- ID: {player['id']}.")
        
        choix = input("Enter the numbers's player (ex: 1,3,5) : ")
        return [int(num.strip()) for num in choix.split(',')]
                
    @staticmethod
    def set_scores_views(match: Any) -> float:
        """ Gère la saisie du score"""

        while True:
            try:
                score1 = float(input(f"Score for {match.joueur1} (0, 0.5, 1) : "))
                if score1 not in {0, 0.5, 1}:
                    raise ValueError
                return score1
            except ValueError:
                print("Error : Enter 0, 0.5 or 1")

    @staticmethod
    def display_debrief(debrief_data):
        """Affiche le debrief à partir des données brutes."""
        print("\n=== DEBRIEF FINAL ===")
        
        # Classement
        print("\n Final Ranking :")
        for idx, player in enumerate(debrief_data["ranking"], 1):
            print(f"{idx}. {player.name} {player.firstname} - {player.score} pts")
        
        # Détails des rounds
        print("\nRound's details  :")
        for round in debrief_data["rounds"]:
            print(f"\n  Round {round.nom} :")
            for match in round.match_list:
                result = "Draw" if match.score1 == 0.5 else \
                        f"Winner: {match.joueur1}" if match.score1 == 1 else \
                        f"Winner: {match.joueur2}"
                print(f"    {match.joueur1} vs {match.joueur2} → {result}")
    
    @staticmethod
    def display_match(match_data, show_result=False):
        """ Partie report, pour avoir les informations d'un tournoi et des rounds """

        joueur1 = f"{match_data['joueur1']['name']} {match_data['joueur1']['firstname']}"
        joueur2 = f"{match_data['joueur2']['name']} {match_data['joueur2']['firstname']}"

        if show_result:
            score1 = match_data.get('score1', 0)
            score2 = match_data.get('score2', 0)
            result = (
                f"Vainqueur: {joueur1}" if score1 > score2 else
                f"Vainqueur: {joueur2}" if score2 > score1 else
                "Match nul"
            )
            print(f"{joueur1} vs {joueur2} → {result}")
        else:
            print(f"{joueur1} vs {joueur2}")

    @staticmethod
    def display_round(round_data): 
        """ Afiche les informations d'un round """

        print(f"\n--- Round {round_data['nom']} ({round_data['dateStart']} à {round_data['dateEnd']}) ---")

    @staticmethod
    def get_tournament_name(): 
        """ Demande le nom d'un tournoi pour accéder au report"""

        return input("Tournament's name to display : ")


