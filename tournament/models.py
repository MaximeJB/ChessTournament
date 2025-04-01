import string
import random
import json
import os
from views import get_user_infos
import views 




def json_players_data():
    """ Charge tous les joueurs présent dans le fichier json """
    player_json = r"C:\Users\maxym\Documents\GitHub\tournament\Playersinfo.json"
    with open(player_json, "r") as json_file:
        internal_data = json.load(json_file)
        return internal_data 


def all_player_json():
    """ Print le nom et prénom de tous les joueurs présent dans le json"""
    data = json_players_data()
    for players in data: 
        print(players["name"], players["firstname"])


def tournaments_data_json():
    """ Print toutes la data de tous les tournois du logiciel """
    tournaments_json =  "tournaments_data.json"
    with open(tournaments_json, "r") as f: 
        current_data = json.load(f)
        return current_data

def all_tournaments_data_json():
    """Print toute la data sur les tournois """
    tournament_data = tournaments_data_json()
    print(tournament_data["Name"])

    

class Joueur:
    """ Représente un joueur et ses données """


    def __init__(self, name, firstname, birthdate):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate

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
                        "birthdate": self.birthdate,
                        } 
    
        file_path = "Playersinfo.json"

        if os.path.exists("Playersinfo.json"):
                with open(file_path, "r") as f:
                    try:
                        players_data = json.load(f)
                        print(players_data)
                    except json.JSONDecodeError:
                        players_data = []
        else : 
            players_data = []


        
        players_data.append(player_infos)

        with open(file_path, "w") as f:
            json.dump(players_data, f, indent=2)
        
        print("Nouveau joueur ajouté avec succès !")
    
def generate_ids():
    numbers = "1234567890"
    random.seed(10)
    letters = string.ascii_uppercase
    rand_letters = random.choices(letters,k=2) # where k is the number of required rand_letters
    first_part = "".join(rand_letters)
    rand_numbers = random.choices(numbers, k=4)
    second_part ="".join(rand_numbers)
    final = first_part + second_part
    print(final)
    
    #Ces identifiants sont uniques et comportent deux lettres suivies de cinq chiffres
# (par exemple, AB12345)

   
class Tournament:
    """ Représente un tournoi, ses informations et ses impact sur les données """


    def __init__(self, name, description,location, dateStart, dateEnd, number_of_rounds=4,):
        self.name = name
        self.description = description
        self.location = location
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.number_of_rounds = number_of_rounds
        self.list_of_players = []
        self.rounds = []
        self.all_rounds = []
    


    def __str__(self):
        """ Représentation de mon tournoi """
        return  (f"""
                 \n
                 \n
                Tournoi : {self.name}, \n
                Lieu : {self.location}
                Dates : du {self.dateStart} au {self.dateEnd}
                Lieu : {self.location}"
                Description : {self.description}"
                Nombre de rounds : {self.number_of_rounds}""")
        
     
    def take_players_from_json(self):
        player_json = r"C:\Users\maxym\Documents\GitHub\tournament\Playersinfo.json"
        with open(player_json, "r") as json_file:
            internal_data = json.load(json_file)
            self.list_of_players = internal_data 
        return self.list_of_players
    

    
    
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
                        """ Méthode anti corruption de fichier, les données 
                        sont chargé avant de réecrire sur le json. """
                        tournaments_data = []
        
        else : 
            tournaments_data = [] 
        tournaments_data.append(tournaments_infos)

        with open(file_path, "w") as f: 
            json.dump(tournaments_data, f, indent=4)
            
        
    def scoring(self):
        print("Qui a gagné ?")
        dashboard = input()
    

    def add_tour(self, tour):
        self.__class__.append(tour)

    def shuffle_and_pairs_players(self):
        """ La logique devrait fonctionner
            Pour l'instant on garde le code le plus simple
            mais il se peut qu'on doive utiliser zip_longest from
            itertools. pour palier à ca."""
        random.shuffle(self.list_of_players)
        paires = list(zip(
        self.list_of_players[::2],
        self.list_of_players[1::2]
        ))
        return paires  
    
class Tour():
    """ Représente un tour, ses joueurs, ses données"""

    def __init__(self, name, dateStart, dateEnd):
        self.nom = name
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.rounds = []
    
    def add_round(self, round):
        self.rounds.append(round)

    def __str__(self):
        return f"""
        The round's name is : {self.nom}
        The round starts : {self.dateStart}
        The round end on : {self.dateEnd}
        Display of all the matches : {self.matches}
        """
    
    def generate_matches_from_pair(self, shuffled_pairs):
        match_list = []
        for pair in shuffled_pairs :
            match = Match(pair)
            match_list.append(match)
        return match_list
        


class Match:
   """ Représente l'instance d'un match, ses joueurs, son score """
   

   def __init__(self, joueur1,joueur2):
         #players = ([instance_players1, score], [instance_players2, score]) 
        self.joueur1 = joueur1, 
        self.joueur2 = joueur2, 
        self.matches = []
        #TODO : Initialiser que lors de la première init un score est toujours 0
        #TODO : Initialiser avec une méthode que si un joueur a gagné un match, il prend +1 sur son score (et le garde)

   def set_final_score(self, score1,score2):
        self.players = ([self.joueur1, score1], [self.joueur2, score2]) 
        

   


   