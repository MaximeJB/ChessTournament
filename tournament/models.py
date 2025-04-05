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

def process_matches(versus):
    for i, match in enumerate(versus, 1):
        # Affichage du match
        views.display_match(
            match_number=i,
            total_matches=len(versus),
            player1=match.joueur1,
            player2=match.joueur2
        )
        
        # Récupération du choix utilisateur
        while True:
            choice = views.get_user_choice()
            if choice in {"1", "2", "3"}:
                break
            print("Choix invalide. Réessayez.")
        
        # Mise à jour des scores
        if choice == "1":
            match.joueur1.score += 1
        elif choice == "2":
            match.joueur2.score += 1
        else:  # Match nul
            match.joueur1.score += 0.5
            match.joueur2.score += 0.5
        
        # Mise à jour des adversaires rencontrés
        match.joueur1.opponents.append(match.joueur2.id)
        match.joueur2.opponents.append(match.joueur1.id)

class Joueur:
    """ Représente un joueur et ses données """


    def __init__(self,player_id, name, firstname, birthdate):
        self.id = player_id
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.score = 0
        self.opponents = []

    def __str__(self):
        return f"{self.name} {self.firstname}"
        
    def to_dict(self):
        # Convertit l'objet Joueur en dictionnaire serializable
        return {
            "id": self.id,
            "name": self.name,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "score" : self.score,
            "opponents" : self.opponents
        }

    def save_to_json(self):
        player_infos = {
                        "id": self.id,
                        "name": self.name,
                        "firstname": self.firstname,
                        "birthdate": self.birthdate,
                        "score" : self.score,
                        "opponents": self.opponents
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

    # Générer un ID unique
    while True:
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices("1234567890", k=5))  
        new_id = letters + numbers
        
        
        return new_id
    
    

   
class Tournament:
    """ Représente un tournoi, ses informations et ses impact sur les données """


    def __init__(self, name, description,location, dateStart, dateEnd, number_of_rounds=4):
        self.name = name
        self.description = description
        self.location = location
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.number_of_rounds = number_of_rounds
        self.list_of_players = []
        self.current_round = []
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
        
            self.list_of_players = [
                Joueur(j["id"],j["name"], j["firstname"], j["birthdate"])
                for j in internal_data
            ]
        return self.list_of_players
    
    def select_players_for_tournament(self):
        all_players = json_players_data()
        print("Players in the database : ")
        for player in all_players:
            print(f"ID: {player["id"]} - {player["name"]} {player["firstname"]}")

        selected_ids = views.choose_players().split(',')
        self.list_of_players = [
            Joueur(player["id"], player["name"], player["firstname"], player["birthdate"])
            for player in all_players if player["id"] in selected_ids
        ]

    
    
    def save_tournament_data(self):
        tournaments_infos = {
                              "name" : self.name,
                              "description": self.description, 
                              "location": self.location, 
                              "Beginning of the tournament" : self.dateStart,
                              "End of tournament" : self.dateEnd,
                              "Numbers of rounds" : self.number_of_rounds,
                              "List of players" : [j.to_dict() for j in self.list_of_players],
                              "Current round" : self.current_round,
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
        self.all_rounds.append(tour)

    def shuffle_and_pairs_players(self):
        """ La logique devrait fonctionner
            Pour l'instant on garde le code le plus simple
            mais il se peut qu'on doive utiliser zip_longest from
            itertools. pour palier à ca."""
        
        # Premier round : mélange aléatoire
        if len(self.all_rounds) == 0:  
            random.shuffle(self.list_of_players)
            return list(zip(self.list_of_players[::2], self.list_of_players[1::2]))
        
        # Pour les rounds suivants
        else:
            # Tri par score décroissant puis par ID pour la stabilité
            sorted_players = sorted(self.list_of_players, 
                                key=lambda x: (-x.score, x.id))
            
            pairs = []
            used = set()
            
            for position, player1 in enumerate(sorted_players):
                if player1 in used:
                    continue
                    
                # Trouver le premier joueur non affronté et non utilisé
                for joueur in range(position+1, len(sorted_players)):
                    player2 = sorted_players[joueur]
                    
                    if (player2 not in used and 
                        player2.id not in player1.opponents):
                        
                        pairs.append((player1, player2))
                        used.update({player1, player2})
                        break
                        
                # Cas où aucun adversaire disponible -> on prend le suivant
                else:
                    if position+1 < len(sorted_players):
                        player2 = sorted_players[position+1]
                        pairs.append((player1, player2))
                        used.update({player1, player2})
            
            return pairs
    
class Tour():
    """ Représente un tour, ses joueurs, ses données"""

    def __init__(self, name, dateStart, dateEnd):
        self.nom = name
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.match_list = []
    

    def __str__(self):
        return f"""
        The round's name is : {self.nom}
        The round starts : {self.dateStart}
        The round end on : {self.dateEnd}
        Display of all the matches : {self.match_list}
        """
    
    def generate_matches_from_pair(self, shuffled_pairs):
        """Initialise les matchs à partir des pairs récupérer dans "shuffle and pairs"
        important : un init de Match passe sur les pairs, les pairs sont rangé dans une liste 
        appelé "match_list" """
        for pair in shuffled_pairs:
            match = Match(pair[0], pair[1])
            self.match_list.append(match)
        return self.match_list
    
    
   
  

class Match:
    """ Représente l'instance d'un match, ses joueurs, son score """
   

    def __init__(self, joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2 
        self.score1 = 0
        self.score2 = 0
        


    def __str__(self):
        return f"""
        
        Le match est entre {self.joueur1} et {self.joueur2} 

"""


   