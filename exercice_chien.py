class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age

    def se_presenter(self):
        print(f"Je m'appelle {self.nom}, je suis un {self.race}, et j'ai {self.age} ans. ")
    def aboyer(self):
        print(f"{self.nom} dit : Woof !")
    
pepper = Chien("Pepper", "Border Collie", 3)
amy = Chien("Amy", "Tervueren", 11)
lucky = Chien("Lucky", "Berger", 9)
zymo = Chien("Zymo", "Berger", 11)

pepper.se_presenter()
amy.se_presenter()
lucky.se_presenter()
zymo.se_presenter()