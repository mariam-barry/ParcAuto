class Client():
    def __init__(self ,id , nom):
        self.id= id
        self.nom = nom
        self.location = []


    def allouer(self, location):
        self.location.append(location)

    def info(self):
        return f" id: {self.id} je suis {self.nom }"
    
    

