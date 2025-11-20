import string
import random
import json
import os
import views


class Json:

    @staticmethod
    def json_players_data():
        """Charge tous les joueurs présent dans le fichier json"""
        file_path = "Players.json"
        players_data = []

        if os.path.exists("Players.json"):
            with open(file_path, "r") as f:
                try:
                    players_data = json.load(f)
                except json.JSONDecodeError:
                    players_data = []
        else:
            file_path = players_data
            players_data = []
            print("La liste des joueurs est vide !")

        return players_data


    @staticmethod
    def all_player_json():
        """Print le nom et prénom de tous les joueurs présent dans le json"""
        data = Json.json_players_data()
        for players in data:
            print(players["name"], players["firstname"])

    @staticmethod
    def tournaments_data_json(tournament_name=None):
        """Retourne UN SEUL tournoi (dict) si nom spécifié, sinon liste complète"""
        dir_path = "tournaments"

        # Recherche ciblée par nom exact
        if tournament_name:
            filename = f"{tournament_name} - Current Data.json"
            file_path = os.path.join(dir_path, filename)

            if not os.path.exists(file_path):
                return None

            try:
                with open(file_path, "r") as f:
                    return json.load(f)  # Retourne directement le dictionnaire
            except Exception as e:
                print(f"Erreur lecture {filename} : {str(e)}")
                return None

        # Chargement de tous les tournois
        all_tournaments = []
        if os.path.exists(dir_path):
            for filename in os.listdir(dir_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(dir_path, filename)
                    try:
                        with open(file_path, "r") as f:
                            all_tournaments.append(json.load(f))
                    except Exception as e:
                        print(f"Erreur avec {filename} : {str(e)}")

        return all_tournaments


    @staticmethod
    def all_tournaments_data_json():
        """Print les noms de tous les tournois"""
        tournament_data = Json.tournaments_data_json()
        print(tournament_data["name"])


    @staticmethod
    def all_tournaments_json():
        """Print le titre de tous les tournois enregistré"""
        for idx, filename in enumerate(os.listdir("tournaments"), 1):
            if filename.endswith(".json"):
                tournament_name = filename.split(" - ")[0]
                print(f"{idx}. {tournament_name}")


class Joueur:
    """Représente un joueur et ses données"""

    def __init__(self, player_id, name, firstname, birthdate):
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
            "score": self.score,
            "opponents": self.opponents,
        }

    def save_to_json(self):
        player_infos = {
            "id": self.id,
            "name": self.name,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "score": self.score,
            "opponents": self.opponents,
        }

        file_path = "Players.json"

        if os.path.exists("Players.json"):
            with open(file_path, "r") as f:
                try:
                    players_data = json.load(f)
                except json.JSONDecodeError:
                    players_data = []
        else:
            players_data = []

        players_data.append(player_infos)

        with open(file_path, "w") as f:
            json.dump(players_data, f, indent=2)

        print("Nouveau joueur ajouté avec succès !")


def generate_ids():

    # Générer un ID unique
    while True:
        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        numbers = "".join(random.choices("1234567890", k=5))
        new_id = letters + numbers

        return new_id


class Tournament:
    """Représente un tournoi, ses informations et ses impact sur les données"""

    def __init__(
        self, name, description, location, dateStart, dateEnd, number_of_rounds=4
    ):
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
        """Représentation de mon tournoi"""
        return f"""
                 \n
                 \n
                Tournoi : {self.name}, \n
                Lieu : {self.location}
                Dates : du {self.dateStart} au {self.dateEnd}
                Lieu : {self.location}"
                Description : {self.description}"
                Nombre de rounds : {self.number_of_rounds}"""

    def take_players_from_json(self):
        file_path = os.path.join("Players.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                internal_data = json.load(json_file)

                self.list_of_players = [
                    Joueur(j["id"], j["name"], j["firstname"], j["birthdate"])
                    for j in internal_data
                ]
        return self.list_of_players

    def add_tour(self, tour):
        """Ajoute le tour a la liste de tous les rounds"""
        self.all_rounds.append(tour)

    def shuffle_and_pairs_players(self):
        """Si c'est un premier round, shuffle l'input et crée des duos. Si c'est pas le premier round"""

        # Premier round : mélange aléatoire
        if len(self.all_rounds) == 0:
            random.shuffle(self.list_of_players)
            return list(zip(self.list_of_players[::2], self.list_of_players[1::2]))

        # Pour les rounds suivants
        else:
            # Tri par score décroissant puis par ID pour la stabilité
            sorted_players = sorted(
                self.list_of_players, key=lambda x: (-x.score, x.id)
            )

            pairs = []
            used = set()

            for position, player1 in enumerate(sorted_players):
                if player1 in used:
                    continue

                # Trouver le premier joueur non affronté et non utilisé
                for joueur in range(position + 1, len(sorted_players)):
                    player2 = sorted_players[joueur]

                    if player2 not in used and player2.id not in player1.opponents:

                        pairs.append((player1, player2))
                        used.update({player1, player2})
                        break

                # Cas où aucun adversaire disponible -> on prend le suivant
                else:
                    if position + 1 < len(sorted_players):
                        player2 = sorted_players[position + 1]
                        pairs.append((player1, player2))
                        used.update({player1, player2})

            return pairs

    def save_current_data_to_json(self):
        """Sauvegarde après chaque round la ou en est le programme"""
        directory = "tournaments"
        file_name = f"{self.name} - Current Data.json"
        file_path = os.path.join(directory, file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        data = {
            "name": self.name,
            "dateStart": f"Tournament started at : {self.dateStart}",
            "dateEnd": f"Tournament ended at : {self.dateEnd}",
            "description": self.description,
            "location": self.location,
            "rounds": [round.to_dict() for round in self.all_rounds],
            "players": [p.to_dict() for p in self.list_of_players],
        }

        try:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)
                print(""" \n ✅ Données du round sauvegardées !""")
        except Exception as e:
            print(f" Erreur lors de la sauvegarde : {str(e)}")

    def select_players_for_tournament(self):
        all_players = Json.json_players_data()
        selected_indices = views.Views.select_players_for_tournament_view(all_players)

        self.list_of_players = [
            Joueur(
                player["id"], player["name"], player["firstname"], player["birthdate"]
            )
            for idx, player in enumerate(all_players, 1)
            if idx in selected_indices  # idx commence à 1
        ]

    def generate_debrief_data(self):
        """Génère les données du debrief (sans formattage)."""
        debrief_data = {
            "ranking": sorted(self.list_of_players, key=lambda p: (-p.score, p.id)),
            "rounds": self.all_rounds,
        }
        return debrief_data

    def print_players_sorted(self):
        sorted_players = sorted(
            self.list_of_players, key=lambda p: (p.name, p.firstname)
        )
        for p in sorted_players:
            print(p.name, p.firstname)


class Tour:
    """Représente un tour, ses joueurs, ses données"""

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
            "match_list": [match.to_dict() for match in self.match_list],
        }

    def generate_matches_from_pair(self, shuffled_pairs):
        """Initialise les matchs à partir des pairs récupérer dans "shuffle and pairs"
        important : un init de Match passe sur les pairs, les pairs sont rangé dans une liste
        appelé "match_list" """
        for pair in shuffled_pairs:
            match = Match(pair[0], pair[1])
            self.match_list.append(match)
        return self.match_list


class Match:
    """Représente l'instance d'un match, ses joueurs, son score"""

    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = 0
        self.score2 = 0
        self.players = ([self.joueur1, self.score1], [self.joueur2, self.score2])

    def to_dict(self):
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "score1": self.score1,
            "score2": self.score2,
        }

    def __str__(self):
        return f"""
        
        The match is between {self.joueur1} and {self.joueur2}\n"""

    def update_scores(self, score1):
        """Gère la saisie des scores et met à jour l'historique des adversaires"""

        self.score1 = score1
        self.score2 = 1 - score1
        self.joueur1.score += self.score1
        self.joueur2.score += self.score2

        # Mise à jour des scores
        self.players = ([self.joueur1, self.score1]), ([self.joueur2, self.score2])

        if self.joueur2.id not in self.joueur1.opponents:
            self.joueur1.opponents.append(self.joueur2.id)

        if self.joueur1.id not in self.joueur2.opponents:
            self.joueur2.opponents.append(self.joueur1.id)
