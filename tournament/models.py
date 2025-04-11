import string
import random
import json
import os
import views 
import datetime
import pdb 


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
    all_tournaments = []
    
    # Vérifie si le dossier existe
    if not os.path.exists("tournaments"):
        return all_tournaments  # Retourne liste vide si dossier inexistant
    
    # Parcourt tous les fichiers .json du dossier
    for filename in os.listdir("tournaments"):
        if filename.endswith(".json"):
            file_path = os.path.join("tournaments", filename)
            try:
                with open(file_path, "r") as f:
                    tournament_data = json.load(f)
                   

                    all_tournaments.append(tournament_data)

            except (json.JSONDecodeError, PermissionError) as e:
                print(f"Erreur avec {filename} : {str(e)}")
    
    return all_tournaments


def all_tournaments_data_json(): 
    """ Print les noms de tous les tournois """
    tournament_data = tournaments_data_json()
    print(tournament_data["name"])

def all_player_json():
    data = json_players_data()
    for player in sorted(data, key=lambda x: (x["name"], x["firstname"])):  # Tri ajouté
        print(player["name"], player["firstname"])


def all_tournaments_json():
    for idx, filename in enumerate(os.listdir("tournaments"), 1):
            if filename.endswith(".json"):
                # Extraction du nom avant le ' - ' pour l'affichage
                tournament_name = filename.split(" - ")[0]
                print(f"{idx}. {tournament_name}")

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
    
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])  # 1. Crée une instance de Player avec le nom du JSON
        player.score = data["score"]  # 2. Attribue le score sauvegardé
        return player  # 3. Renvoie le joueur reconstruit
    
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
    
    
    
    
    def save_tournament_data(self):
        tournaments_infos = {
                              "name" : self.name,
                              "description": self.description, 
                              "location": self.location, 
                              "dateStart" : self.dateStart,
                              "dateEnd" : self.dateEnd,
                              "Numbers of rounds" : self.number_of_rounds,
                              "List of players" : [j.to_dict() for j in self.list_of_players],
                              "current_round": self.current_round.to_dict() if self.current_round else None,
                              "all_rounds": [round.to_dict() for round in self.all_rounds]
        }

        os.makedirs("tournaments", exist_ok=True)

        filename = f"{self.name} - {self.dateStart}.json".replace(":", "-").replace(" ", "_")
        file_path = os.path.join("tournaments", filename)  # <-- Correction clé ici
        

        with open(file_path, "w") as f: 
            json.dump(tournaments_infos, f, indent=4)
            
        

    def add_tour(self, tour):
        """ Ajoute le tour a la liste de tous les rounds """
        self.all_rounds.append(tour)

    def shuffle_and_pairs_players(self):
        """Si c'est un premier round, shuffle l'input et crée des duos. Si c'est pas le premier round
            """
        
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
        
    def save_current_data_to_json(self):
        x = datetime.datetime.now()
        sorted_players = sorted(self.list_of_players, key=lambda p: -p.score)
        current_tournament_infos = {
            "tournament_name" : self.name,
            "date" : f" Tournament started at : {x.strftime("%c")}",
            "rounds" : [round.to_dict() for round in self.all_rounds],
            "current ranking" : [player.to_dict() for player in sorted_players]
        }
       
    
        file_path = f"{self.name} - {x.strftime("%c")} - Current Data .json"

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists("Tournament_Data_In_real_time.json"):
            with open(file_path, "r") as f:
                try : 
                    tournament_data_in_real_time = json.load(f)
                    print(tournament_data_in_real_time)
                except json.JSONDecodeError:
                    tournament_data_in_real_time = []
        else : 
            tournament_data_in_real_time = []

        tournament_data_in_real_time = current_tournament_infos
        with open(file_path,"w") as f:
            json.dump(tournament_data_in_real_time,f,indent=2)
            print("Tournoi sauvegardé")

    @classmethod
    def load_from_json(cls, filename):
            with open(filename, "r") as f:  # 1. Ouvre le fichier en lecture
                data = json.load(f)  # 2. Charge le JSON en dictionnaire `data`
            
            # 3. Crée une instance de Tournament avec le nom du JSON
            tournament = cls(data["tournament_name"])
            
            # 4. Recrée la liste des joueurs avec leurs scores
            tournament.list_of_players = [Joueur.from_dict(p) for p in data["current_ranking"]]
            
            # 5. Recrée chaque round en passant la liste des joueurs existants
            tournament.all_rounds = [
                Tour.from_dict(r, tournament.list_of_players)  # 6. Utilise les joueurs du tournoi
                for r in data["rounds"]
            ]
            
            return tournament  # 7. Renvoie le tournoi entièrement reconstruit
    
    def select_players_for_tournament(self):
        all_players = json_players_data()
        selected_indices = views.select_players_for_tournament_view(all_players)  
        
        self.list_of_players = [
            Joueur(player["id"], player["name"], player["firstname"], player["birthdate"])
            for idx, player in enumerate(all_players, 1) if idx in selected_indices  # idx commence à 1
        ]

    def generate_debrief_data(self):
        """Génère les données du debrief (sans formattage)."""
        debrief_data = {
            "ranking": sorted(self.list_of_players, key=lambda p: (-p.score, p.id)),
            "rounds": self.all_rounds
        }
        return debrief_data
    
    def print_players_sorted(self):
        sorted_players = sorted(self.list_of_players, key=lambda p: (p.name, p.firstname))
        for p in sorted_players:
                print(p.name, p.firstname)

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
    
    def to_dict(self):
        return {
            "nom": self.nom,
            "dateStart": self.dateStart,
            "dateEnd": self.dateEnd,
            "match_list": [match.to_dict() for match in self.match_list]
        }

    def generate_matches_from_pair(self, shuffled_pairs):
        """Initialise les matchs à partir des pairs récupérer dans "shuffle and pairs"
        important : un init de Match passe sur les pairs, les pairs sont rangé dans une liste 
        appelé "match_list" """
        for pair in shuffled_pairs:
            match = Match(pair[0], pair[1])
            self.match_list.append(match)
        return self.match_list
    
    @classmethod
    def from_dict(cls, data, players):  # 1. Prend les données du round + la liste des joueurs
        round = cls(data["round_name"])  # 2. Crée un Round avec son nom
        for match_data in data["matches"]:  # 3. Pour chaque match dans les données
            # 4. Trouve le joueur 1 dans la liste `players` par son nom
            player1 = next(p for p in players if p.name == match_data["player1"])
            # 5. Trouve le joueur 2 de la même manière
            player2 = next(p for p in players if p.name == match_data["player2"])
            # 6. Crée un Match avec les joueurs et le score
            match = Match(player1, player2, tuple(match_data["score"]))
            round.match_list.append(match)  # 7. Ajoute le match au round
        return round  # 8. Renvoie le round reconstruit
    
class Match:
    """ Représente l'instance d'un match, ses joueurs, son score """
   

    def __init__(self, joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2 
        self.score1 = 0
        self.score2 = 0
        
    def to_dict(self):
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "score1": self.score1,
            "score2": self.score2
        }

    def __str__(self):
        return f"""
        
        Le match est entre {self.joueur1} et {self.joueur2}  """

    def set_scores(self):
        """Gère la saisie des scores et met à jour l'historique des adversaires"""
        
        print(f"\n--- Match : {self.joueur1} vs {self.joueur2} ---")
        
    
        score1 = views.set_scores_views(self)
        

        self.score1 = score1
        self.score2 = 1 - score1  
                                
        
        # Mise à jour des scores
        self.joueur1.score += self.score1
        self.joueur2.score += self.score2
        
    
        if self.joueur2.id not in self.joueur1.opponents:
            self.joueur1.opponents.append(self.joueur2.id)
        
        if self.joueur1.id not in self.joueur2.opponents:
            self.joueur2.opponents.append(self.joueur1.id)

    ##TODO : finir la gestion des bonnes données (verifications des données, validation)
    ##TODO : formattage du report des tournois (option 3 et 4 sur le report)
    ##TODO : mettre en place le controller et le views dans des classes (staticmethod)
