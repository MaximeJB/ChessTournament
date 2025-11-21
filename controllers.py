import os
from views import Views
from models import Joueur, Json, Tournament, Tour, generate_ids


class Controllers:
    """Classe regroupant les fonctions de contrôle de l'application."""

    @staticmethod
    def start_player_management() -> None:
        """Gère le menu de gestion des joueurs.

        Permet d'ajouter de nouveaux joueurs ou de revenir au menu principal.
        Boucle jusqu'à ce que l'utilisateur choisisse de quitter.

        Returns:
            None
        """
        while True:
            Views.clear_screen()
            Views.display_user_management_menu()
            user_choice = Views.get_user_choice()
            if user_choice == "1":
                while True:
                    Views.clear_screen()
                    user_infos = Views.get_user_infos()
                    player_id = generate_ids()
                    new_player = Joueur(player_id=player_id, **user_infos)
                    new_player.save_to_json()
                    Views.clear_screen()
                    Views.another_player()
                    answers = Views.get_user_choice()
                    if answers in {"2", "3"}:
                        break
                    elif answers == "1":
                        continue
            elif user_choice == "2":
                Controllers.run()

    @staticmethod
    def display_report_controller():
        """Gère le menu des rapports et l'affichage des données.

        Affiche les joueurs, tournois, détails de tournois ou rounds/matchs.
        Boucle jusqu'à ce que l'utilisateur choisisse de quitter.

        Returns:
            None
        """
        while True:
            Views.report_menu()
            user_choice = Views.get_user_choice()
            if user_choice == "1":
                Json.all_player_json()
                Views.report_menu()
                user_choice = Views.get_user_choice()
                if user_choice == "5":
                    break

            elif user_choice == "2":
                Views.clear_screen()
                Json.all_tournaments_json()
                break

            elif user_choice == "3":
                tournament_name = input("Tournament's name : ").strip()
                tournament_data = Json.tournaments_data_json(tournament_name)

                if not tournament_data:
                    print(f"\n Aucun tournoi nommé '{tournament_name}' trouvé.")
                    return

                print("\n" + "=" * 50)
                print(f"Nom : {tournament_data['name']}")
                print(
                    f"{tournament_data['dateStart']} until {tournament_data['dateEnd']}"
                )
                print(f"Location : {tournament_data['location']}")
                print(f"Description : {tournament_data['description']}")
                print("=" * 50)

            elif user_choice == "4":
                tournament_name = Views.get_tournament_name()
                data = Json.tournaments_data_json()
                tournament_found = False
                for tournament in data:
                    if tournament.get("name") == tournament_name:
                        tournament_found = True
                        for round in tournament.get(
                            "rounds", tournament.get("all_rounds", [])
                        ):
                            Views.display_round(round)

                            for match in round.get("match_list", []):
                                Views.display_match(match, show_result=True)
                        break

                if not tournament_found:
                    Views.tournament_not_found_error(tournament_name)

            elif user_choice == "5":
                Views.clear_screen()
                break

    @staticmethod
    def create_tournament_controller():
        """Gère la création et l'exécution complète d'un tournoi.

        Permet de créer un tournoi, sélectionner les joueurs, exécuter tous les rounds,
        enregistrer les scores et afficher le classement final.

        Returns:
            None
        """
        while True:
            Views.clear_screen()
            Views.menu_tournament()
            user_choice = Views.get_user_choice()

            if user_choice == "1":
                Views.clear_screen()
                tournament_data = Views.get_tournament_infos()
                tournament = Tournament(
                    **tournament_data
                )  # instanciation de mon tournament
                Views.clear_screen()
                Views.tournament_successfully_added()
                user_choice = Views.get_user_choice()

                if user_choice == "1":
                    # Player selection logic (moved from models to controller)
                    all_players = Json.json_players_data()
                    selected_indices = Views.select_players_for_tournament_view(all_players)
                    tournament.list_of_players = [
                        Joueur(
                            player["id"], player["name"], player["firstname"], player["birthdate"]
                        )
                        for player_number, player in enumerate(all_players, 1)
                        if player_number in selected_indices
                    ]
                    tournament.save_current_data_to_json()
                    Views.clear_screen()

                    for i in range(tournament.number_of_rounds):

                        shuffle_players = tournament.shuffle_and_pairs_players()
                        round_data = Views.get_round_infos()
                        Views.clear_screen()
                        round = Tour(**round_data)  # instanciation de mon round
                        versus = round.generate_matches_from_pair(
                            shuffle_players
                        )  # instanciation de match

                        for match in versus:
                            print(match)
                            Views.clear_screen()
                        for match in versus:
                            score1 = Views.set_scores_views(match)
                            match.update_scores(score1)

                        tournament.add_tour(round)
                        tournament.save_current_data_to_json()
                        Views.clear_screen()

                    debrief_data = tournament.generate_debrief_data()  # Modèle
                    Views.display_debrief(debrief_data)  # Vue
                    tournament.save_current_data_to_json()
                elif user_choice == "2":
                    break
            elif user_choice == "2":
                Controllers.run()

    @staticmethod
    def exit_program() -> None:
        """Ferme le programme proprement.

        Affiche un message de fermeture et termine l'exécution.

        Returns:
            None
        """
        Views.exit_message()
        exit()

    @staticmethod
    def run() -> None:
        """Exécute la boucle principale du programme.

        Affiche le menu principal et redirige vers les différents contrôleurs
        selon le choix de l'utilisateur.

        Returns:
            None
        """
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            Views.display_menu()
            user_choice = Views.get_user_choice()
            if user_choice == "1":
                Controllers.create_tournament_controller()
            elif user_choice == "2":
                Controllers.start_player_management()
            elif user_choice == "3":
                Views.clear_screen()
                Controllers.display_report_controller()
            elif user_choice == "4":
                Controllers.exit_program()


if __name__ == "__main__":
    Controllers.run()
