from abc import ABC , abstractmethod

class Vehicule( ABC):
    def __init__(self , marque , modele , annee , disponible):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._disponible = disponible
        self.location = []


    @property
    def marque(self):
        return self._marque
    
    @property
    def modele(self):
        return self._modele
    
    @property
    def annee(self):
        return self._annee
    

    @property
    def disponible(self):
        return self._disponible
    
    @marque.setter
    def marque(self, marque):
        self._marque = marque


    @modele.setter
    def modele(self, modele):
        self._modele = modele


    @annee.setter
    def annee(self, annee):
        self._annee = annee

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible

    @abstractmethod
    def afficher_info(self):
        pass


    def allouer(self, location):
        self.location.append(location)


    def louer(self):
        self._disponible = False
        return self._disponible
        
    
    def rendre(self):
        self._disponible = True
        return self._disponible
       
    
    def est_disponible(self):
        return self._disponible                                                                                                                                     

        
    
        
    
      

class Voiture(Vehicule):
  
    def __init__(self, marque, modele, annee, disopnible, nb_portes ):
       super().__init__(marque, modele, annee, disopnible)
       self.nb_portes = nb_portes 

    def afficher_info(self):
       return f"  marque : {self._marque}  , modele : {self._modele} annee: {self._annee}   {'disponible' if self._disponible else 'indisponible'} nb_portes  : {self.nb_portes}"



 
    
class Camion(Vehicule):
    def __init__(self, marque, modele, annee, disopnible , capacite):
        super().__init__(marque, modele, annee, disopnible)
        self.capacite = capacite 


    def afficher_info(self):
       return  f"  marque : {self._marque}  , modele : {self._modele} annee: {self._annee}  disponible : {self._disponible}  capacite  :  {self.capacite} "



  

