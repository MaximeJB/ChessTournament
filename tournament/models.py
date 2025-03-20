import string
import random
import json
from views import get_user_infos


def json_players_data():
    """ Enregistre tous les joueurs présent dans le logiciel dans un json """
    player_json = r"C:\Users\maxym\Documents\GitHub\tournament\Playersinfo.json"
    with open(player_json, "r") as json_file:
        internal_data = json.load(json_file)
        return internal_data 


def all_player_json():
    """ Print le nom et prénom de tous les joueurs présent dans le json"""
    data = json_players_data()
    print(data["name"], data["firstname"])

def tournaments_data_json():
    """ Print toutes la data de tous les tournois du logiciel (à verifier)"""
    tournaments_json =  
    

class Joueur:
    def __init__(self, user_infos):
        self.name = user_infos["Name"]
        self.firstname = user_infos["Firstname"]
        self.birthdate = user_infos["Birthdate"]

    def __str__(self):
        return self.name + " " + self.firstname + " " + self.birthdate
        

    # def __str__(self, listes_joueurs):
    #     Joueur.listes_joueurs = listes_joueurs
    #     return f"{self.nom} {self.prenom} (Elo: {self.elo})"

   
# """ 
#         """ else : 
#             print(f"{new_player} est déjà inscrit à la compétition") """ """

    def save_to_json(self):
        player_infos = {
                        "name": self.name,
                        "firstname": self.firstname,
                        "birthdate": self.birthdate}
    
        json_data = json.dumps(player_infos, indent=2)
        f = open("Playersinfo.json", "a")
        f.write(json_data)
        f.close()

   



class Tournament:
    """ Représente un tournoi, ses informations et ses impact sur les données """

    def __init__(self, name, location, dateStart, dateEnd,description, number_of_rounds=4,):
        self.name = name
        self.description = description
        self.location = location
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.number_of_rounds = number_of_rounds
        self.list_of_players = []
        self.rounds = []
        self.all_rounds = []
    
    def start():
        pass

    def save_tournament_data(self):
        tournaments_infos = { "name" : self.name,
                              "description": self.description, 
                              "location": self.location, 
                              "Beginning of the tournament" : self.dateStart,
                              "End of tournament" : self.dateEnd,
                              "Numbers of rounds" : self.number_of_rounds,
                              "List of players" : self.list_of_players,
                              "Current round" : self.rounds,
                              "List of rounds" : self.all_rounds
        }

        file_path = "tournaments.data.json"
        with open(file_path, "a") as f:
            tournament_json_data = json.dumps(tournaments_infos, indent=2)
            f.write(tournament_json_data)
    ##TODO : le json est corrompu de cette manière, faire en sorte qu'il soit 
        #    initialiser de nouveau et recréer si on le réouvre. voir deepseek.

    def scoring():
        print("Qui a gagné ?")
        dashboard = input()
    
    def add_player(self, new_player):
        ###TODO : la l'idée serait d'aller prendre un player dans le json et de l'ajouter à une instance de tournois, et donc nouveau 
        ###       json pour les données de self.tournoi
        self.new_player = new_player
        

# la je dois faire une méthode ou le gagnant gagnerait de l'elo 
# ou une variable victory et 
# passerait au prochain tour

    def add_tour(self, tour):
        self.__class__.append(tour)


        
class Tour():
    matches = []
    dateEnd = None
    dateStart = None 

    def __init__(self, nom, dateStart):
        self.nom = nom
        self.dateStart = dateStart
    
    def add_match(self, match):
        self.matches.append(match)
    

class Match:
   match = []

    # players = ([instance_players1, score], [instance_players2, score]) 
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        
        Joueur.add_player(joueur1)
        Joueur.add_player(joueur2)

        self.__class__.append(joueur1)
        self.__class__.append(joueur2)


    def score(self):
        pass