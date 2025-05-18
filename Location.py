from date import Date


class Location():
    def __init__(self , date_debut , date_fin , vehicule , client):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.vehicule = vehicule
        self.client = client

        client.allouer(self)
        vehicule.allouer(self)


    def duree(self):
        return self.date_fin.difference(self.date_debut)
    
    def afficher(self):
        print(" les informations de la location : ")
        return f" date de location : {self.date_debut.to_string()}  , date de rendu : {self.date_fin.to_string()}  pour le vehicule {self.vehicule.marque} du client : {self.client.nom}"

    def calcul_prix(self):
       
        return f"le prix  est :  { 50 * self.duree()} " 