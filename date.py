from  datetime import  date
class Date():
    def __init__(self ,jour , mois , annee):
        self.jour= jour
        self.mois = mois
        self.annee = annee
        self._date = date(annee, mois, jour)
        

    def to_string(self):
         return self._date.strftime("%d/%m/%Y")
    
    def difference(self , autre):
       
        return (self._date - autre._date).days
        

    