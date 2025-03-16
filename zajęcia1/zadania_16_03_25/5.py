class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent
    def __str__(self):
        return f"{self.producent} {self.model}"

class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca:Telefon, tresc):
        print( f"Wysylanie do {odbiorca}, treść: {tresc}")
class Rozrywka:
    def odtworz_muzyke(self, utwor):
        print( f"Odtwarzanie utworu {utwor} ▶️")
class Smartphone(Telefon,Komunikacja,Rozrywka):
    def __init__(self, model, producent):
        super().__init__(model, producent)
smartphone1= Smartphone("16", "Iphone")
smartphone2 = Smartphone("A52S", "Samsung")

smartphone1.odtworz_muzyke("tralalala")
smartphone1.wyslij_wiadomosc(smartphone2,"halo halo, wiadomość")