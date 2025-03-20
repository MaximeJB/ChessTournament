import string
import random
import json
import os
from views import get_user_infos


def json_players_data():
    """ Charge tous les joueurs présent dans le fichier json"""
    player_json = r"C:\Users\maxym\Documents\GitHub\tournament\Playersinfo.json"
    with open(player_json, "r") as json_file:
        internal_data = json.load(json_file)
        return internal_data 


def all_player_json():
    """ Print le nom et prénom de tous les joueurs présent dans le json"""
    data = json_players_data()
    print(data["name"], data["firstname"])


def tournaments_data_json():
    """ Print toutes la data de tous les tournois du logiciel"""
    tournaments_json =  "tournaments_data.json"
    with open(tournaments_json, "r") as f: 
        current_data = json.load(f)
        return current_data

def all_tournaments_data_json():
    """Print toute la data sur les tournois"""
    tournament_data = tournaments_data_json()
    print(tournament_data["Name"])

    

class Joueur:
    """ Représente un joueur et ses données """


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
                        "birthdate": self.birthdate
                        }
    
        file_path = "Playersinfo.json"

        if os.path.exists("Playersinfo.json"):
                with open(file_path, "r") as f:
                    try:
                        players_data = json.load(f)
                    except json.JSONDecodeError:
                        players_data = []
        else : 
            players_data = []


        
        players_data.append(player_infos)

        with open(file_path, "w") as f:
            json.dump(players_data, f, indent=2)
        
        print("Nouveau joueur ajouté avec succès !")
       

   
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
        tournaments_infos = {
                              "name" : self.name,
                              "description": self.description, 
                              "location": self.location, 
                              "Beginning of the tournament" : self.dateStart,
                              "End of tournament" : self.dateEnd,
                              "Numbers of rounds" : self.number_of_rounds,
                              "List of players" : self.list_of_players,
                              "Current round" : self.rounds,
                              "List of rounds" : self.all_rounds
        }

        file_path = "tournaments_data.json"
        if os.path.exists("tournaments_data.json"):
                with open(file_path, "r") as f:
                    try:
                        tournaments_data = json.load(f)
                    except json.JSONDecodeError:
                        tournaments_data = []
        
        else : 
        #Méthode anti corruption de fichier, si le fichier existe, je le charge
        #et j'écris dessus. si il n'existe pas ou est corrompu, il est 
        #rénitialisier avec une nouvelle liste.
            tournaments_data = [] 

        tournaments_data.append(tournaments_infos)

        with open(file_path, "w") as f: 
            json.dump(tournaments_data, f, indent=4)
            
        print("Tournoi sauvegardé avec succès !")
        




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
    """ Représente un tour, ses joueurs, ses données"""

    matches = []
    dateEnd = None
    dateStart = None 


    def __init__(self, nom, dateStart):
        self.nom = nom
        self.dateStart = dateStart
    
    def add_match(self, match):
        self.matches.append(match)
    

class Match:
   """ Représente l'instance d'un match, ses joueurs, son score """
   match = []


    #players = ([instance_players1, score], [instance_players2, score]) 
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        
        Joueur.add_player(joueur1)
        Joueur.add_player(joueur2)

        self.__class__.append(joueur1)
        self.__class__.append(joueur2)


    def score(self):
        pass