import os
from views import Views
from models import Joueur, Json, Tournament, Tour, generate_ids
from typing import Any



class Controllers:
    """ Classe regroupant les fonctions de contrôle de l'application."""

    @staticmethod
    def start_player_management() -> None:
        """ Contrôle de gestion des joueurs"""

        while True :
            Views.display_user_management_menu()
            user_choice = Views.get_user_choice()
            if user_choice == "1":
                while True :
                    user_infos =  Views.get_user_infos()
                    player_id = generate_ids()
                    new_player = Joueur(player_id = player_id, **user_infos) 
                    new_player.save_to_json()
                    Views.another_player()
                    answers = Views.get_user_choice()
                    if answers in {"2", "3"}:
                        break
                    elif answers =="1":
                        continue
            elif user_choice == "2":
                Controllers.run()

            
   
        
                

    @staticmethod
    def display_report_controller():
        """ Gère l'affichage des rapports"""

        while True : 
            Views.report_menu()
            user_choice = Views.get_user_choice()
            if user_choice == "1":
                    Json.all_player_json()
                    Views.report_menu()
                    user_choice = Views.get_user_choice()
                    if user_choice == "5":
                        break
            elif user_choice == "2":
                Json.all_tournaments_json()
                break

            elif user_choice == "3":
                tournament_name = input("Tournament's name : ")
                data = Json.tournaments_data_json()
                for t in data:
                    if t["name"] == tournament_name:
                        print(f"Dates : {t.get('dateStart', 'N/A')} au {t.get('dateEnd', 'N/A')}")
                        break

            elif user_choice == "4":
                tournament_name = Views.get_tournament_name() 
                data = Json.tournaments_data_json()        
                for tournament in data:
                    if tournament["name"] == tournament_name:  
                
                        for round in tournament["all_rounds"]:
                            Views.display_round(round)  
                    
                            for match in round["match_list"]:
                                Views.display_match(match)  
                                break
            elif user_choice =="5":
                break

            

    @staticmethod
    def create_tournament_controller():
            """ Gère la création et manipulation d'un tournoi"""

            while True:
                Views.menu_tournament()
                user_choice = Views.get_user_choice()

                if user_choice == "1":
                        tournament_data = Views.get_tournament_infos()
                        tournament = Tournament(**tournament_data) #instanciation de mon tournament
                        Views.tournament_successfully_added()
                        user_choice = Views.get_user_choice()

                        if user_choice =="1":
                            tournament.select_players_for_tournament()
                            tournament.save_tournament_data()

                            for i in range(tournament.number_of_rounds):

                                shuffle_players = tournament.shuffle_and_pairs_players()
                                round_data = Views.get_round_infos()
                                round = Tour(**round_data) #instanciation de mon round
                                versus = round.generate_matches_from_pair(shuffle_players) #instanciation de match

                                for match in versus :
                                    print(match)   
                                print("Enter the results: ")
                                for match in versus : 
                                    match.set_scores()

                                tournament.add_tour(round)
                                tournament.save_current_data_to_json()

                            debrief_data = tournament.generate_debrief_data()  # Modèle
                            Views.display_debrief(debrief_data)  # Vue
                            tournament.save_tournament_data()
                        elif user_choice == "2":
                            break
                elif user_choice == "2":
                    Controllers.run()






    @staticmethod
    def exit_program() -> None:
        print(" >>> You closed the program.")
        exit()


    def run() -> None:
        """ Execute la boucle principale du programme"""
        os.system("cls")
        while True : 
            Views.display_menu()
            user_choice = Views.get_user_choice()
            if user_choice ==  "1" :
                Controllers.create_tournament_controller()
            elif user_choice == "2":
                Controllers.start_player_management()
            elif user_choice == "3":
                Controllers.display_report_controller()
            elif user_choice == "4":
                Controllers.exit_program()




if __name__ == "__main__":
    Controllers.run()