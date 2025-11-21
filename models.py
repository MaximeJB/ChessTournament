import string
import random
import json
import os


PLAYERS_FILE = "Players.json"
TOURNAMENTS_DIR = "tournaments"
TOURNAMENT_FILE_SUFFIX = " - Current Data.json"


class Json:
    """Classe utilitaire pour la gestion des fichiers JSON."""

    @staticmethod
    def json_players_data():
        """Charge tous les joueurs depuis le fichier JSON.

        Returns:
            list[dict]: Liste des joueurs avec leurs données (id, name, firstname, birthdate, score, opponents).
                       Retourne une liste vide si le fichier n'existe pas ou est invalide.
        """
        file_path = PLAYERS_FILE
        players_data = []

        if os.path.exists(PLAYERS_FILE):
            with open(file_path, "r") as f:
                try:
                    players_data = json.load(f)
                except json.JSONDecodeError:
                    players_data = []
        else:
            file_path = players_data
            print("La liste des joueurs est vide !")

        return players_data


    @staticmethod
    def all_player_json():
        """Affiche le nom et prénom de tous les joueurs.

        Returns:
            None: Affiche directement dans la console.
        """
        data = Json.json_players_data()
        for players in data:
            print(players["name"], players["firstname"])

    @staticmethod
    def tournaments_data_json(tournament_name=None):
        """Charge un ou plusieurs tournois depuis le dossier tournaments.

        Args:
            tournament_name (str, optional): Nom du tournoi à charger.
                Si None, charge tous les tournois. Defaults to None.

        Returns:
            dict | list[dict] | None:
                - Si tournament_name fourni: dict du tournoi ou None si non trouvé
                - Si tournament_name=None: liste de tous les tournois
        """
        dir_path = TOURNAMENTS_DIR

        
        if tournament_name:
            filename = f"{tournament_name}{TOURNAMENT_FILE_SUFFIX}"
            file_path = os.path.join(dir_path, filename)

            if not os.path.exists(file_path):
                return None

            try:
                with open(file_path, "r") as f:
                    return json.load(f)  
            except Exception as e:
                print(f"Erreur lecture {filename} : {str(e)}")
                return None

        
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
        """Affiche les noms de tous les tournois.

        Returns:
            None: Affiche directement dans la console.
        """
        tournament_data = Json.tournaments_data_json()
        for tournament in tournament_data:
            print(tournament["name"])


    @staticmethod
    def all_tournaments_json():
        """Affiche la liste numérotée de tous les tournois.

        Returns:
            None: Affiche directement dans la console au format "1. Tournament Name".
        """
        for idx, filename in enumerate(os.listdir(TOURNAMENTS_DIR), 1):
            if filename.endswith(".json"):
                tournament_name = filename.split(" - ")[0]
                print(f"{idx}. {tournament_name}")


class Joueur:
    """Représente un joueur et ses données.

    Attributes:
        id (str): Identifiant unique du joueur.
        name (str): Nom de famille du joueur.
        firstname (str): Prénom du joueur.
        birthdate (str): Date de naissance du joueur.
        score (float): Score total du joueur dans le tournoi.
        opponents (list[str]): Liste des IDs des adversaires déjà affrontés.
    """

    def __init__(self, player_id, name, firstname, birthdate):
        """Initialise un nouveau joueur.

        Args:
            player_id (str): Identifiant unique du joueur.
            name (str): Nom de famille.
            firstname (str): Prénom.
            birthdate (str): Date de naissance.
        """
        self.id = player_id
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.score = 0
        self.opponents = []

    def __str__(self):
        return f"{self.name} {self.firstname}"

    def to_dict(self):
        """Convertit l'objet Joueur en dictionnaire JSON serializable.

        Returns:
            dict: Dictionnaire contenant toutes les données du joueur.
        """
        return {
            "id": self.id,
            "name": self.name,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "score": self.score,
            "opponents": self.opponents,
        }

    def save_to_json(self):
        """Sauvegarde le joueur dans le fichier Players.json.

        Ajoute le joueur à la liste existante ou crée un nouveau fichier.

        Returns:
            None: Affiche un message de confirmation après sauvegarde.
        """
        player_infos = {
            "id": self.id,
            "name": self.name,
            "firstname": self.firstname,
            "birthdate": self.birthdate,
            "score": self.score,
            "opponents": self.opponents,
        }

        file_path = PLAYERS_FILE

        if os.path.exists(PLAYERS_FILE):
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
    """Génère un identifiant unique aléatoire pour un joueur.

    Format: 2 lettres majuscules + 5 chiffres (ex: AB12345).

    Returns:
        str: Identifiant unique généré.
    """
    while True:
        letters = "".join(random.choices(string.ascii_uppercase, k=2))
        numbers = "".join(random.choices("1234567890", k=5))
        new_id = letters + numbers

        return new_id


class Tournament:
    """Représente un tournoi d'échecs complet.

    Attributes:
        name (str): Nom du tournoi.
        description (str): Description du tournoi.
        location (str): Lieu du tournoi.
        dateStart (str): Date de début.
        dateEnd (str): Date de fin.
        number_of_rounds (int): Nombre de rounds (défaut: 4).
        list_of_players (list[Joueur]): Liste des joueurs participants.
        current_round (list): Round en cours.
        all_rounds (list[Tour]): Historique de tous les rounds.
    """

    def __init__(
        self, name, description, location, dateStart, dateEnd, number_of_rounds=4
    ):
        """Initialise un nouveau tournoi.

        Args:
            name (str): Nom du tournoi.
            description (str): Description du tournoi.
            location (str): Lieu du tournoi.
            dateStart (str): Date de début.
            dateEnd (str): Date de fin.
            number_of_rounds (int, optional): Nombre de rounds. Defaults to 4.
        """
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
        return f"""Tournoi : {self.name}
                    Lieu : {self.location}
                    Dates : du {self.dateStart} au {self.dateEnd}
                    Description : {self.description}
                    Nombre de rounds : {self.number_of_rounds}"""

    def take_players_from_json(self):
        """Charge tous les joueurs depuis Players.json dans le tournoi.

        Returns:
            list[Joueur]: Liste des joueurs chargés.
        """
        file_path = PLAYERS_FILE
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                internal_data = json.load(json_file)

                self.list_of_players = [
                    Joueur(j["id"], j["name"], j["firstname"], j["birthdate"])
                    for j in internal_data
                ]
        return self.list_of_players

    def add_tour(self, tour):
        """Ajoute un round terminé à l'historique du tournoi.

        Args:
            tour (Tour): Le round à ajouter.

        Returns:
            None
        """
        self.all_rounds.append(tour)

    def shuffle_and_pairs_players(self):
        """Crée les paires de joueurs pour un round selon le système suisse.

        Premier round: Mélange aléatoire des joueurs.
        Rounds suivants: Appariement par score (évite les rematches si possible).

        Returns:
            list[tuple[Joueur, Joueur]]: Liste de paires de joueurs.
        """
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
        """Sauvegarde l'état actuel du tournoi dans un fichier JSON.

        Crée ou met à jour le fichier tournoi dans le dossier tournaments/.

        Returns:
            None: Affiche un message de confirmation ou d'erreur.
        """
        directory = TOURNAMENTS_DIR
        file_name = f"{self.name}{TOURNAMENT_FILE_SUFFIX}"
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

    def generate_debrief_data(self):
        """Génère les données du rapport final du tournoi.

        Returns:
            dict: Dictionnaire contenant le classement final et les rounds.
                {
                    "ranking": list[Joueur] (triés par score décroissant),
                    "rounds": list[Tour]
                }
        """
        debrief_data = {
            "ranking": sorted(self.list_of_players, key=lambda p: (-p.score, p.id)),
            "rounds": self.all_rounds,
        }
        return debrief_data

    def print_players_sorted(self):
        """Affiche les joueurs triés alphabétiquement par nom puis prénom.

        Returns:
            None: Affiche directement dans la console.
        """
        sorted_players = sorted(
            self.list_of_players, key=lambda p: (p.name, p.firstname)
        )
        for p in sorted_players:
            print(p.name, p.firstname)


class Tour:
    """Représente un round du tournoi.

    Attributes:
        name (str): Nom du round (ex: "Round 1").
        dateStart (str): Date/heure de début du round.
        dateEnd (str): Date/heure de fin du round.
        match_list (list[Match]): Liste des matchs du round.
    """

    def __init__(self, name, dateStart, dateEnd):
        """Initialise un nouveau round.

        Args:
            name (str): Nom du round.
            dateStart (str): Date/heure de début.
            dateEnd (str): Date/heure de fin.
        """
        self.name = name
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.match_list = []

    def __str__(self):
        return f"""
        The round's name is : {self.name}
        The round starts : {self.dateStart}
        The round end on : {self.dateEnd}
        Display of all the matches : {self.match_list}
        """

    def to_dict(self):
        """Convertit le round en dictionnaire JSON serializable.

        Returns:
            dict: Dictionnaire contenant les données du round et ses matchs.
        """
        return {
            "name": self.name,
            "dateStart": self.dateStart,
            "dateEnd": self.dateEnd,
            "match_list": [match.to_dict() for match in self.match_list],
        }

    def generate_matches_from_pair(self, shuffled_pairs):
        """Initialise les matchs à partir des paires de joueurs.

        Args:
            shuffled_pairs (list[tuple[Joueur, Joueur]]): Liste de paires de joueurs.

        Returns:
            list[Match]: Liste des matchs créés et ajoutés à match_list.
        """
        for pair in shuffled_pairs:
            match = Match(pair[0], pair[1])
            self.match_list.append(match)
        return self.match_list


class Match:
    """Représente un match entre deux joueurs.

    Attributes:
        joueur1 (Joueur): Premier joueur.
        joueur2 (Joueur): Second joueur.
        score1 (float): Score du joueur 1 (0, 0.5, ou 1).
        score2 (float): Score du joueur 2 (0, 0.5, ou 1).
    """

    def __init__(self, joueur1, joueur2):
        """Initialise un nouveau match.

        Args:
            joueur1 (Joueur): Premier joueur.
            joueur2 (Joueur): Second joueur.
        """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = 0
        self.score2 = 0

    def to_dict(self):
        """Convertit le match en dictionnaire JSON serializable.

        Returns:
            dict: Dictionnaire contenant les joueurs et leurs scores.
        """
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
        """Met à jour les scores du match et l'historique des adversaires.

        Calcule automatiquement score2 = 1 - score1.
        Met à jour les scores cumulés et l'historique des adversaires de chaque joueur.

        Args:
            score1 (float): Score du joueur 1 (0 = défaite, 0.5 = match nul, 1 = victoire).

        Returns:
            None
        """

        self.score1 = score1
        self.score2 = 1 - score1
        self.joueur1.score += self.score1
        self.joueur2.score += self.score2

        if self.joueur2.id not in self.joueur1.opponents:
            self.joueur1.opponents.append(self.joueur2.id)

        if self.joueur1.id not in self.joueur2.opponents:
            self.joueur2.opponents.append(self.joueur1.id)
