import string
import random
import json


class Joueur:
    def __init__(self,name,firstname):
        self.name = name
        self.firstname = firstname

    def __str__(self):
        return self.name + " " + self.firstname
        

    """ def __str__(self, listes_joueurs):
        Joueur.listes_joueurs = listes_joueurs
        return f"{self.nom} {self.prenom} (Elo: {self.elo})" """

    def add_player(self, new_player):
        pass 

        """ else : 
            print(f"{new_player} est déjà inscrit à la compétition") """

    def save_to_json(self):
        player_infos = {
                        "name": self.name,
                        "firstname": self.firstname,
                        }
    
    
        json_data = json.dumps(player_infos, indent=2)
        f = open("Playersinfo.json", "a")
        f.write(json_data)
        f.close()

    def remove_player(self,joueurs):
        self.joueurs= joueurs
        Joueur.listes_joueurs.remove(joueurs)



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
    dateStart = None 

    def __init__(self, nom, dateStart):
        self.nom = nom
        self.dateStart = dateStart
    
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
        pass