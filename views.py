"""Module views avec tous les prints de l'application"""

from typing import Any, Dict
from datetime import datetime
import re
import platform
import os


class Views:
    """Classe statique regroupant toutes les méthodes de vues de l'application"""

    @staticmethod
    def display_menu() -> None:
        """Affiche le menu principal de l'application.

        Returns:
            None
        """
        print(
            """
                Main Menu 

        - 1.Create a Tournement
        - 2.Player Management
        - 3.Reports
        - 4.Quit

    """
        )

    @staticmethod
    def get_user_choice() -> str:
        """Demande et retourne le choix de l'utilisateur.

        Returns:
            str: Le choix saisi par l'utilisateur.
        """
        choice = input(">>>  ")
        return choice

    @staticmethod
    def display_user_management_menu() -> None:
        """Affiche le menu de gestion des joueurs.

        Returns:
            None
        """
        print(
            """
           
            Do you want to :

            -1.Add a player
            -2.Main Menu  

            """
        )

    @staticmethod
    def another_player() -> None:
        """Demande si l'utilisateur veut ajouter un autre joueur.

        Returns:
            None
        """
        print(
            """
        Do you want to add another player ? 
        
                    -1.Yes 
                    -2.No 
                    -3.Main Menu"""
        )

    @staticmethod
    def get_user_infos() -> Dict[str, str]:
        """Récupère les informations d'un nouveau joueur.

        Demande à l'utilisateur de saisir nom, prénom et date de naissance.

        Returns:
            dict: Dictionnaire avec les clés "name", "firstname", "birthdate".
        """
        player_infos = {
            "name": Views.input_with_validator("\n What's your name ? ", str),
            "firstname": Views.input_with_validator("What's your first name ?  ", str),
            "birthdate": Views.input_with_validator("What's your birthdate ?  ", str),
        }
        return player_infos

    @staticmethod
    def report_menu() -> None:
        """Affiche le menu des rapports.

        Returns:
            None
        """
        print(
            """
                Report Menu
                
            -1.List of all players
            -2.List of all tournaments
            -3.Tournaments data 
            -4.Access list of rounds for each tournaments and matches for each rounds.
            -5.Main Menu
                
    """
        )

    @staticmethod
    def menu_tournament() -> None:
        """Affiche le menu du tournoi.

        Returns:
            None
        """
        print(
            """ 
            Tournament dashboard 
            
            1.Create a new tournament
            2.Back to Main Menu
            
            """
        )

    @staticmethod
    def input_with_validator(prompt: str, data_type: Any) -> Any:
        """Valide et retourne une saisie utilisateur selon le type attendu.

        Gère la validation des chaînes, entiers, dates et accepte des raccourcis
        pour les dates (aujourd'hui, demain, hier).

        Args:
            prompt (str): Message à afficher à l'utilisateur.
            data_type (Any): Type de données attendu (str, int, etc.).

        Returns:
            Any: La valeur saisie et validée selon le type.
        """
        while True:
            text = input(prompt).strip()

            
            if data_type == str and (
                "date" in prompt.lower()
                or "start" in prompt.lower()
                or "end" in prompt.lower()
            ):
                if len(text) == 10 and text[2] == "." and text[5] == ".":
                    try:
                        formatted_date = Views.parse_date(text)
                        if formatted_date:
                            return formatted_date
                    except ValueError:
                        print("Invalid date (e.g., 30.02.2000 doesn't exist)")
                else:
                    print("Expected format: DD.MM.YYYY (e.g., 05.05.2000)")
                continue

            try:
                if data_type == str:
                    if not text.isdigit():  
                        return text
                    raise ValueError("Text expected, not number")

                elif data_type == int:
                    return int(text)

                elif data_type == float:
                    return float(text)

            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    @staticmethod
    def parse_date(date_string: str):
        """Analyse et formate une chaîne de date.

        Accepte plusieurs formats de dates et retourne au format DD/MM/YYYY.
        Gère les raccourcis: aujourd'hui, demain, hier.

        Args:
            date_string (str): Date à analyser (format DD.MM.YYYY ou raccourci).

        Returns:
            str | None: Date formatée DD/MM/YYYY ou None si format invalide.
        """
        
        date_formats = [
            (r"^(\d{1,2})[/.-](\d{1,2})[/.-](\d{4})$", "%d/%m/%Y"),
            (r"^(\d{4})[/.-](\d{1,2})[/.-](\d{1,2})$", "%Y/%m/%d"),
            (r"^(\d{1,2})[/.-](\d{1,2})[/.-](\d{2})$", "%d/%m/%y"),
        ]

        for pattern, date_format in date_formats:
            match = re.match(pattern, date_string)
            if match:
                try:
                    # Adapter le format selon la regex qui a matché
                    if date_format == "%d/%m/%Y":
                        day, month, year = match.groups()
                        date_obj = datetime(int(year), int(month), int(day))
                    elif date_format == "%Y/%m/%d":
                        year, month, day = match.groups()
                        date_obj = datetime(int(year), int(month), int(day))
                    elif date_format == "%d/%m/%y":
                        day, month, year = match.groups()
                        # Pour les années à 2 chiffres, on suppose 2000+
                        year = int(year)
                        if year < 70:  # Hypothèse: années inférieures à 70 sont 2000+
                            year += 2000
                        else:
                            year += 1900
                        date_obj = datetime(year, int(month), int(day))

                    
                    return date_obj.strftime("%d/%m/%Y")
                except ValueError:
                    continue

        
        text_dates = {
            "aujourd'hui": datetime.now(),
            "demain": datetime.now().replace(day=datetime.now().day + 1),
            "hier": datetime.now().replace(day=datetime.now().day - 1),
        }

        lower_date = date_string.lower()
        if lower_date in text_dates:
            return text_dates[lower_date].strftime("%d/%m/%Y")

        return None

    @staticmethod
    def get_tournament_infos() -> Dict[str, Any]:
        """Récupère les informations pour créer un tournoi.

        Demande à l'utilisateur de saisir toutes les informations nécessaires.

        Returns:
            dict: Dictionnaire avec les clés name, description, location, dateStart, dateEnd, number_of_rounds.
        """
        tournament_infos = {
            "name": Views.input_with_validator(
                "What's the name of the tournament ?  ", str
            ),
            "description": Views.input_with_validator(
                "What's the tournament description ?  ", str
            ),
            "location": Views.input_with_validator(
                "What's the tournament location ?  ", str
            ),
            "dateStart": Views.input_with_validator(
                "When does the tournament start ?  ", str
            ),
            "dateEnd": Views.input_with_validator(
                "When does the tournament end ? ", str
            ),
            "number_of_rounds": Views.input_with_validator(
                "How many rounds ? (per default = 4)  ", int
            ),
        }
        return tournament_infos

    @staticmethod
    def get_round_infos() -> Dict[str, str]:
        """Récupère les informations pour créer un round.

        Demande le nom, la date de début et la date de fin du round.

        Returns:
            dict: Dictionnaire avec les clés name, dateStart, dateEnd.
        """
        round_info = {
            "name": Views.input_with_validator(
                """\n      
            What's the name of the round ? :  """,
                str,
            ),
            "dateStart": Views.input_with_validator(
                """
            When does it start ? :  """,
                str,
            ),
            "dateEnd": Views.input_with_validator(
                """
            When does it end ? :  """,
                str,
            ),
        }
        return round_info

    @staticmethod
    def tournament_successfully_added() -> None:
        """Affiche la confirmation de création du tournoi.

        Demande si l'utilisateur veut démarrer le premier round.

        Returns:
            None
        """
        print(
            """ 
                
                The tournament was sucessfully created ! 
                Do you want to create the first round ?   

                -1.Yes 
                -2.No (Main Menu)
                
                """
        )

    @staticmethod
    def select_players_for_tournament_view(players):
        """Affiche la liste de joueurs et récupère la sélection.

        Args:
            players (list[dict]): Liste des joueurs disponibles.

        Returns:
            list[int]: Liste des numéros des joueurs sélectionnés.
        """
        print("\n--- Select Player ---")
        for idx, player in enumerate(players, 1):
            print(
                f"{idx} - {player['name']} {player['firstname']} -- ID: {player['id']}."
            )

        choix = input("Enter the numbers's player (ex: 1,3,5) : ")
        return [int(num.strip()) for num in choix.split(",")]

    @staticmethod
    def set_scores_views(match: Any) -> float:
        """Demande et valide la saisie du score d'un match.

        Args:
            match (Match): Le match pour lequel saisir le score.

        Returns:
            float: Score du joueur 1 (0, 0.5, ou 1).
        """
        print("\n" + "=" * 50)
        print("\n     ENTER THE SCORE : ")
        print(f"\n--- Match : {match.joueur1} VS {match.joueur2} ---\n")
        print("\n" + "=" * 50)
        while True:
            try:
                score1 = float(input(f"Score for {match.joueur1} (0, 0.5, or 1) : "))
                if score1 not in {0, 0.5, 1}:
                    raise ValueError
                Views.clear_screen()
                return score1
            except ValueError:
                print("Error : Enter 0, 0.5 or 1")

    @staticmethod
    def display_debrief(debrief_data):
        """Affiche le rapport final du tournoi.

        Affiche le classement des joueurs et les résultats de tous les matchs.

        Args:
            debrief_data (dict): Dictionnaire avec "ranking" (joueurs triés) et "rounds" (tous les rounds).

        Returns:
            None
        """
        print("\n=== DEBRIEF FINAL ===")

        
        print("\n Final Ranking :")
        for idx, player in enumerate(debrief_data["ranking"], 1):
            print(f"{idx}. {player.name} {player.firstname} - {player.score} pts")

        print("\nRound's details  :")
        for round in debrief_data["rounds"]:
            print(f"\n  Round {round.name} :")
            for match in round.match_list:
                result = (
                    "Draw"
                    if match.score1 == 0.5
                    else (
                        f"Winner: {match.joueur1}"
                        if match.score1 == 1
                        else f"Winner: {match.joueur2}"
                    )
                )
                print(f"    {match.joueur1} vs {match.joueur2} → {result}")

    @staticmethod
    def display_match(match_data, show_result=False):
        """Affiche les informations d'un match.

        Args:
            match_data (dict): Données du match avec joueur1, joueur2, score1, score2.
            show_result (bool, optional): Si True, affiche le résultat. Defaults to False.

        Returns:
            None
        """
        joueur1 = (
            f"{match_data['joueur1']['name']} {match_data['joueur1']['firstname']}"
        )
        joueur2 = (
            f"{match_data['joueur2']['name']} {match_data['joueur2']['firstname']}"
        )

        if show_result:
            score1 = match_data.get("score1", 0)
            score2 = match_data.get("score2", 0)
            result = (
                f"Vainqueur: {joueur1}"
                if score1 > score2
                else f"Vainqueur: {joueur2}" if score2 > score1 else "Match nul"
            )
            print(f"{joueur1} vs {joueur2} → {result}")
        else:
            print(f"{joueur1} vs {joueur2}")

    @staticmethod
    def display_round(round_data):
        """Affiche les informations d'un round.

        Args:
            round_data (dict): Données du round avec name, dateStart, dateEnd.

        Returns:
            None
        """
        print(
            f"\n--- Round {round_data.get('nom', 'Inconnu')} "
            f"({round_data.get('dateStart', '??/??/????')} à "
            f"{round_data.get('dateEnd', '??/??/????')}) ---"
        )

    @staticmethod
    def get_tournament_name():
        """Demande le nom d'un tournoi à afficher.

        Returns:
            str: Le nom du tournoi saisi par l'utilisateur.
        """
        return input("Tournament's name to display : ")

    @staticmethod
    def clear_screen():
        """Efface l'écran de la console.

        Compatible Windows et Unix/Linux.

        Returns:
            None
        """
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def tournament_not_found_error(tournament_name):
        """Affiche un message d'erreur pour un tournoi introuvable.

        Args:
            tournament_name (str): Nom du tournoi recherché.

        Returns:
            None
        """
        print(f"\nAucun tournoi nommé '{tournament_name}' n'a été trouvé.")
        input("\nAppuyez sur Entrée pour continuer...")

    @staticmethod
    def exit_message():
        """Affiche un message de fermeture du programme.

        Returns:
            None
        """
        print(" >>> You closed the program.")
