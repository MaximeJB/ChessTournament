import os
from views import display_menu, get_user_choice, display_user_management_menu, get_user_infos, another_player, report_menu
from models import Joueur, all_player_json


def start_player_management():
    display_user_management_menu()
    user_choice = get_user_choice()
    while user_choice == "1":
        user_infos =  get_user_infos()
        new_player = Joueur(user_infos)
        new_player.save_to_json()
        print("Le nouveau joueur a été ajouté")
        another_player()
        user_choice = get_user_choice()
        if user_choice == "1":
            user_infos = get_user_infos()
            new_player = Joueur(user_infos["Name"], user_infos["Firstname"], user_infos["Birthdate"])
            new_player.save_to_json()
            print("Le nouveau joueur a été ajouté")
        elif user_choice == "2":
            display_menu()


def display_report_controller():
    report_menu()
    user_choice = get_user_choice()
    if user_choice == "1":
        all_player_json()
        report_menu()
    user_choice = get_user_choice()
    if user_choice == "2":
        all_tournaments_json()
        report_menu()


        


def create_tournament_controller():
    print("Start tournament")

def exit_program():
    print("You closed the program")
    exit()


def run():
    os.system("cls")


    # Display a menu with the options
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
        # 2 - Sort players randomly if the first round 
        # 3 - Sort players by their scoring
        # 4 - Create matches for the round (If two players have the same score then we can put then together,)

        # One player can only play once with another player during the tournament

        # 4 - For each round, enter the scores of the matches

    # 2 - Player Management
        # 1 - Add Player in the database
        

    # 3 - Reports
        # List of all players by alphabetical order
        # List of all tournaments
        # Names and dates of each tournaments
        # List of the tours by tournaments and the matches by tours
            


if __name__ == "__main__":
    run()