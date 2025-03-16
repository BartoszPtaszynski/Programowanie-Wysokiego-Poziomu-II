import json


class AplikacjaMobilna:
    liczba_pobran = 0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja
        self.nowe_pobranie()

    @classmethod
    def nowe_pobranie(cls):
        cls.liczba_pobran = cls.liczba_pobran + 1

    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            dane = json.load(f)
        return cls(dane["nazwa"], dane["wersja"])


aplikacja = AplikacjaMobilna.z_json("app.json")

print(aplikacja.nazwa + " "+aplikacja.wersja)
print(AplikacjaMobilna.ile_pobran())