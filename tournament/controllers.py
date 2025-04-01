import os
from views import display_menu, get_user_choice, display_user_management_menu, get_user_infos, another_player, report_menu, menu_tournament, get_tournament_infos
from views import tournament_successfully_added
from models import Joueur, all_player_json, Tournament, Tour, Match 
import sys 
import views
import models
impor




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
                elif answers == "3":
                    break
                elif answers =="1":
                    user_infos =  get_user_infos()
                    new_player = Joueur(**user_infos) 
                    new_player.save_to_json()
                    break
        elif user_choice =="2":
            break
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
        while True:
            menu_tournament()
            user_choice = get_user_choice()
            if user_choice == "1":
                    tournament_data = get_tournament_infos()
                    tournament = Tournament(**tournament_data)
                    tournament_successfully_added()
                    user_choice = get_user_choice()
                    if user_choice =="1":
                        models.Tournament.take_players_from_json(tournament)
                        models.Tournament.save_tournament_data(tournament)
                        #prendre la liste des participants
                        
                        shuffle_players = models.Tournament.shuffle_and_pairs_players(tournament)
                        round_data = views.get_round_infos()
                        first_round = Tour(**round_data) #la je l'init
                        Tour.add_round(first_round) #la j'ajoute le round a la liste round
                        Tour.__str__ #la je l'affiche
                        models.Tour.generate_matches_from_pair(shuffle_players)
                        views.enter_score()
                        get_user_choice()



            elif user_choice == "2":
                break

#Il me faut une boucle. Pour chaque pair matches.append(match)
#ou matches = () <--- tuple 
#for each match in shuffle_players
# matches += match
#le append est surment mieux pck += va coller les données

#Je me suis arreté sur la création de organize_first_round
#dans models.py, et son imbrication pour la suite du programme
#Je dois écrire l'initialisation des matchs a partir des données
#que je récupère dans Tour. (une possible solution est ecrite
#dans la boucle juste au dessus)

            




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