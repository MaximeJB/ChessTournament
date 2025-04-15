
""" Module views avec tous les prints de l'application """
from typing import Any, Dict
from datetime import date

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
    def input_with_validator(prompt: str, data_type: type) -> Any:
        """
        Demande une saisie à l'utilisateur en validant son type.

        """ 
        
        data_is_valid = False
        value: Any = None

        while not data_is_valid:
            text = input(prompt)
            if data_type == str:
                # On considère valide toute saisie non numérique
                data_is_valid = not text.isdigit()
                value = text
            elif data_type == int:
                try:
                    value = int(text)
                    data_is_valid = True
                except ValueError:
                    data_is_valid = False
                    print("Invalid Input")
            elif data_type == float:
                try:
                    value = float(text)
                    data_is_valid = True
                except ValueError:
                    data_is_valid = False
            # Possibilité d'ajouter d'autres validateurs (ex: date) en fonction de vos besoins.
            if not data_is_valid:
                print("Invalid input. Please try again.")
        return value

    @staticmethod    
    def get_tournament_infos() -> Dict[str, Any]:
            tournament_infos = {
                        "name" : Views.input_with_validator("What's the name of the tournament ?  ", str),
                        "description" : Views.input_with_validator("What's the tournament description ?  ", str),
                        "location" : Views.input_with_validator("What's the tournament location ?  ", str),
                        "dateStart" : Views.input_with_validator("When does the tournament start ? format ""XX.XX.XXXX""  ", float),
                        "dateEnd" : Views.input_with_validator("When does the tournament end ? ", float),
                        "number_of_rounds" : Views.input_with_validator("How many rounds ? (per default = 4)  ", int)
            }
            return tournament_infos

    @staticmethod
    def get_round_infos() -> Dict[str,str]:
        """ Récupère et retourne les informations d'un round, sert à l'init."""

        round_info = {
            "name" : Views.input_with_validator(""" 
                            What's the name of the round ? :  """, str),
            "dateStart" : Views.input_with_validator("When does it start ? format ""XX.XX.XXXX"":  ", float),
            "dateEnd" : Views.input_with_validator("When does it end ? :  ", float)
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
    def display_match(match_data):
        """ Partie report, pour avoir les informations d'un tournoi et des rounds """

        print(f"{match_data['joueur1']['name']} {match_data['joueur1']['firstname']} vs {match_data['joueur2']['name']} {match_data['joueur2']['firstname']}")

    @staticmethod
    def display_round(round_data): 
        """ Afiche les informations d'un round """

        print(f"\n--- Round {round_data['nom']} ({round_data['dateStart']} à {round_data['dateEnd']}) ---")

    @staticmethod
    def get_tournament_name(): 
        """ Demande le nom d'un tournoi pour accéder au report"""

        return input("Tournament's name to display : ")


