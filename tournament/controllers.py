import os
from views import display_menu, get_user_choice, display_user_management_menu, get_user_infos, another_player, report_menu, menu_tournament, get_tournament_infos
from views import tournament_successfully_added
from models import Joueur, all_player_json, Tournament, Tour, generate_ids
import views
import models





def start_player_management():
    while True :
        display_user_management_menu()
        user_choice = get_user_choice()
        if user_choice == "1":
            while True :
                user_infos =  get_user_infos()
                player_id = generate_ids()
                new_player = Joueur(player_id = player_id, **user_infos) 
                new_player.save_to_json()
                another_player()
                answers = get_user_choice()
                if answers == "2":
                    break
                elif answers == "3":
                    break
                elif answers =="1":
                    user_infos =  get_user_infos()
                    player_id = generate_ids()
                    new_player = Joueur(player_id = player_id, **user_infos) 
                    new_player.save_to_json()
                    break
        elif user_choice =="2":
            break
        
    
            


def display_report_controller():
    while True : 
        report_menu()
        user_choice = get_user_choice()
        if user_choice == "1":
                all_player_json()
                report_menu()
                user_choice = get_user_choice()
                if user_choice == "5":
                    break
        elif user_choice == "2":
            models.all_tournaments_json()
            report_menu()

        elif user_choice == "3":
            tournament_name = input("Nom du tournoi : ")
            data = models.tournaments_data_json()
            for t in data:
                if t["name"] == tournament_name:
                    print(f"Dates : {t.get('dateStart', 'N/A')} au {t.get('dateEnd', 'N/A')}")

        elif user_choice == "4":
            tournament_name = views.get_tournament_name() 
            data = models.tournaments_data_json()        
            for tournament in data:
                if tournament["name"] == tournament_name:  
            
                    for round in tournament["all_rounds"]:
                        views.display_round(round)  
                
                        for match in round["match_list"]:
                            views.display_match(match)  

        elif user_choice =="5":
            break

        


def create_tournament_controller():
        while True:
            menu_tournament()
            user_choice = get_user_choice()

            if user_choice == "1":
                    tournament_data = get_tournament_infos()
                    tournament = Tournament(**tournament_data) #instanciation de mon tournament
                    tournament_successfully_added()
                    user_choice = get_user_choice()

                    if user_choice =="1":
                        tournament.select_players_for_tournament()
                        tournament.save_tournament_data()

                        for i in range(tournament.number_of_rounds):

                            shuffle_players = tournament.shuffle_and_pairs_players()
                            round_data = views.get_round_infos()
                            round = Tour(**round_data) #instanciation de mon round
                            versus = round.generate_matches_from_pair(shuffle_players) #instanciation de match

                            for match in versus :
                                print(match)   
                            print("Enters the results : ")
                            for match in versus : 
                                match.set_scores()

                            tournament.add_tour(round)
                            tournament.save_current_data_to_json 

                        debrief_data = tournament.generate_debrief_data()  # Modèle
                        views.display_debrief(debrief_data)  # Vue
                        tournament.save_tournament_data()


""" for i in range (tournament.number_of_rounds):
                            for tour in tournament.all_rounds:
                                print(tour)
                                for match in tour.match_list:
                                    print(match)"""


##TODO : sauvegarder les tounrois en entier dans un json. sauvegarder tournoi a la fin du tournoi
##TODO : sauvegarder le tournoi a chaque fois qu'on crée un round, 
##TODO : formatter le debrief pour montrer les vainqueurs, montrer les matchs pour chaque tour, qui a gagné qui a perdu
##TODO : finir la partie report 
##TODO : faire le readme du projet, expliquer le projet, comment créer un environnement virtuel, comment installer les dépendances du projet
##TODO : faire des classes pour contenir toutes les fonctions de controllers, classe pour contenir tout les views
            




def exit_program():
    print("You closed the program")
    exit()


def run():
    os.system("cls")
    while True : 
        display_menu()
        user_choice = get_user_choice()
        if user_choice ==  "1" :
            create_tournament_controller()
        elif user_choice == "2":
            start_player_management()
        elif user_choice == "3":
            display_report_controller()
        elif user_choice == "4":
            exit_program()




if __name__ == "__main__":
    run()