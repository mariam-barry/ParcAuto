from date import Date
from Location import Location
from Vehicule import Vehicule, Voiture, Camion
from Client import Client
from parc_auto import ParcAuto


def main():
   

    # Creation des véhicules
    Voiture1 = Voiture("Toyota", "Corolla", 2023, True, 4)
    voiture2 = Voiture("Honda", "Civic", 2022, True, 4)
    camion1 = Camion("Actros", "DAF", 2020, True, 150)
    camion2 = Camion("FH16", "Volvo", 2021, False, 180)

    # Creation des clients
    client1 = Client(1, "Barry")
    client2 = Client(2, "Kadi")
    client3 = Client(3, "Ibrahim")

    # Creation des dates
    date1 = Date(2, 10, 2019)
    date2 = Date(23, 8, 2015)
    date3 = Date(11, 4, 2003)

    # Creation des locations
    location = Location(date2, date1, Voiture1, client1)
    location1 = Location(date3, date1, camion1, client2)

    # Creation du parc automobile
    parc = ParcAuto()
    parc.ajouter_vehicule(Voiture1)
    parc.ajouter_vehicule(camion1)
    parc.ajouter_vehicule(voiture2)
    parc.ajouter_vehicule(camion2)

    # Affichage
    parc.lister_disponible()
    parc.rechercher("DAF")

    print(location.afficher())
    print(location.calcul_prix())

    print(location1.afficher())
    print(location1.calcul_prix())


if __name__ == "__main__":
    main()
