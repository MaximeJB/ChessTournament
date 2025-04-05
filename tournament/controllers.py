import os
from views import display_menu, get_user_choice, display_user_management_menu, get_user_infos, another_player, report_menu, menu_tournament, get_tournament_infos
from views import tournament_successfully_added
from models import Joueur, all_player_json, Tournament, Tour, generate_ids
import models
import views





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


def set_scores(match):
    """Gère la saisie des scores et met à jour l'historique des adversaires"""
    
    print(f"\n--- Match : {match.joueur1} vs {match.joueur2} ---")
    
    # Validation des scores avec boucle de contrôle
    ##TODO : Spliter pour mettre l'input en vue
    while True:
        try:
            score1 = float(input(f"Score pour {match.joueur1} (0, 0.5, 1) : "))
            if score1 not in {0, 0.5, 1}:
                raise ValueError
            break
        except ValueError:
            print("Erreur : Entrez uniquement 0, 0.5 ou 1")

    match.score1 = score1
    match.score2 = 1 - score1  # Garantit que la somme vaut toujours 1
                                #Si score = 1, score2 = 0
                                #sI Score1 = 0.5, 1-0.5 = 0.5
                                #si score1 = 0. 1-0 = 1
    
    # Mise à jour des scores
    match.joueur1.score += match.score1
    match.joueur2.score += match.score2
    
    # Ajout des adversaires (avec vérification de doublon)
    if match.joueur2.id not in match.joueur1.opponents:
        match.joueur1.opponents.append(match.joueur2.id)
    
    if match.joueur1.id not in match.joueur2.opponents:
        match.joueur2.opponents.append(match.joueur1.id)
        


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
                        tournament.select_players_for_tournament()
                        tournament.save_tournament_data()
                        for i in range(tournament.number_of_rounds):
                            shuffle_players = tournament.shuffle_and_pairs_players()
                            round_data = views.get_round_infos()
                            round = Tour(**round_data) #la je l'init
                            versus = round.generate_matches_from_pair(shuffle_players)
                            for match in versus :
                                print(match)   
                            print("Enters the results : ")
                            for match in versus : 
                                set_scores(match)
                               # round.add_match(match) # l'instance round ajoute les match dans une liste de match
                            tournament.add_tour(round) #la j'ajoute le round a la liste round
                        for i in range (tournament.number_of_rounds):
                            for tour in tournament.all_rounds:
                                print(tour)
                                for match in tour.match_list:
                                    print(match)




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


        


    """  # 1 - Add player to the tournament """
    """    # 2 - Sort players random2ly if the first round """
        # 3 - Sort players by their scoring after their firsts matches
        # 4 - Create matches for the round (If two players have the same score then we can put then together,)

        # /!\ One player can only play once with another player during the tournament /!\

        # 4 - For each round, enter the scores of the matches

    """ # 2 - Player Management
        # 1 - Add Player in the database """
        

    # 3 - Reports
        # List of all players by alphabetical order
        # List of all tournaments
        # Names and dates of each tournaments
        # List of the tours by tournaments and the matches by tours
            


if __name__ == "__main__":
    run()