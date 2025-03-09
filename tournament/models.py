class Joueur:

    listes_joueurs = []
    id_test = 0
    random_elo = print(f"Sans elo")

    def __init__(self, id,nom,prenom,elo):
        if id is None: Joueur.id_test += 1 
        else : self.id = id
        
#TODO : créer dans le bon format l'identifiant national d'echec

        self.id = id
        self.nom = nom
        self.prenom = prenom

        if elo is None: Joueur.random_elo
        else: self.elo = elo

    def __str__(self, listes_joueurs):
        Joueur.listes_joueurs = listes_joueurs
        return f"{self.nom} {self.prenom} (Elo: {self.elo})"

    def add_player(self, new_player):

        if new_player not in Joueur.listes_joueurs:
            Joueur.listes_joueurs.append(new_player)
        else : 
            print(f"{new_player} est déjà inscrit à la compétition")

    def remove_player(self,joueurs):
        self.joueurs= joueurs
        joueurs.listes_joueurs.remove(joueurs)

    def format_joueurs(self,new_player):
        super().__init__()
        self.id, self.nom, self.prenom, self.elo = new_player.split(",")



class Tournois:
    tours = []

    def __init__(self, name, location, debut, fin,listes_joueurs,description, numero_tours=4):
        self.name = name
        self.description = description
        self.location = location
        self.debut = debut
        self.fin = fin
        self.numero_tours = numero_tours
        self.listes_joueurs = listes_joueurs
    
    def start():
        pass

    def scoring():
        print("Qui a gagné ?")
        dashboard = input()
# la je dois faire une méthode ou le gagnant gagnerait de l'elo 
# ou une variable victory et 
# passerait au prochain tour

    def add_tour(self, tour):
        self.tours.append(tour)


        
class Tour():
    matches = []
    dateEnd = None

    def __init__(self, nom, dateStart):
        self.nom = nom
    
    def add_match(self, match):
        self.matches.append(match)
    

class Match:
    
    # players = ([instance_players1, score], [instance_players2, score])
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

        self.players.append(joueur1)
        self.players.append(joueur2)
    
    def score(self):


def jsons():
    open("json_file.json", "r" , mode = str,)
#TODO : un fichier json par tournoi dans data/tournament



