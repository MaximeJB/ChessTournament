import os
from views import display_menu, get_user_choice, display_user_management_menu, get_user_infos, another_player, report_menu, menu_tournament, start_randomization_first_rounds, get_tournament_infos
from views import tournament_successfully_added
from models import Joueur, all_player_json, Tournament, Tour, Match 
import sys 
import views
import models



def start_player_management():
    while True :
        display_user_management_menu()
        user_choice = get_user_choice()
        if user_choice == "1":
            while True :
                user_infos =  get_user_infos()
                new_player = Joueur(**user_infos) 
                new_player.save_to_json()
                another_player()
                answers = get_user_choice()
                if answers == "2":
                    break
        elif user_choice =="2":
            False
            display_menu
        elif user_choice == "3":
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
            all_tournaments_json()
            report_menu()

        elif user_choice == "3":
            pass 

        elif user_choice == "4":
            pass

        elif user_choice =="5":
            break


        


def create_tournament_controller():
        menu_tournament()
        user_choice = get_user_choice()
        if user_choice == "1":
                tournament_data = get_tournament_infos()
                tournament = Tournament(**tournament_data)
                tournament_successfully_added()
                models.Tournament.take_players_from_json(tournament)
                models.Tournament.save_tournament_data(tournament)
                print("Liste des joueurs après chargement :", tournament.list_of_players)


        
            


               



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


        


        # 1 - Add player to the tournament
        # 2 - Sort players random2ly if the first round 
        # 3 - Sort players by their scoring after their firsts matches
        # 4 - Create matches for the round (If two players have the same score then we can put then together,)

        # /!\ One player can only play once with another player during the tournament /!\

        # 4 - For each round, enter the scores of the matches

    # 2 - Player Management
        # 1 - Add Player in the database
        

    # 3 - Reports
        # List of all players by alphabetical order
        # List of all tournaments
        # Names and dates of each tournaments
        # List of the tours by tournaments and the matches by tours
            
#           VENDREDI : 
##TODO : Créer une fonction pour prendre les joueurs dans le json Joueur et 
#         les ajouter au tournoi.
##TODO : Creer le premier tour. c'est a dire imbriquer joueur, tournois, et tour. 
#        surement via des instances Tour.start_first_round()
#TODO : Randomiser les joueurs, créer le tuple. avoir un print du round et de ses infos
#TODO : créer second round, input du vainqueur, affichage des scores 

if __name__ == "__main__":
    run()