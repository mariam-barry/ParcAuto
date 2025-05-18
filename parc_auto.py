class ParcAuto():
    def __init__(self):
        self.vehicules = []


    def ajouter_vehicule(self , vehicule):
        self.vehicules.append(vehicule)

    def lister_disponible(self):
       print(" les vehicules disponibles sont : ")
       for i in self.vehicules:
           if i.disponible:
               print(i.afficher_info()) 

    def rechercher(self, modele):
        print("resultat pour votre recherche par model : ")
        B=False
        for vehicule in self.vehicules:
            if vehicule.modele == modele :
                print(vehicule.afficher_info()) 
            B = True
        if  B == False:
                print("aucun vehicule trouve avec ce model : ")

        
        

        
