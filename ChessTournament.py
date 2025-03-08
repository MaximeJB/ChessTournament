class Joueur:

    listes_joueurs = []
    id_test = 0
    random_elo = print(f"Sans elo")

    def __init__(self, id,nom,prenom,elo):
        if id is None: Joueur.id_test += 1 
        else : self.id = id

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
    description = "ceci est une description des règles du tournois"
        
    def __init__(self, tours, debut, fin, numero_tours, listes_joueurs):
        self.tours = tours
        self.debut = debut
        self.fin = fin
        self.numero_tours = numero_tours
        self.listes_joueurs = listes_joueurs

class Tour(Tournois):
    def __init__(self, joueur1, joueur2, score):
        self.score = score
        self.joueurs1 = joueur1
        self.joueur2 = joueur2
        
        

def json():
    open("json_file.json", "r" , mode = str,)



j1 = Joueur(1,"Maxime", "JB", 1500)
j2 = Joueur(2,"Maia","Bertin", 1500)

j1.add_player(j1)
j2.add_player(j2)
print(Joueur.listes_joueurs)

