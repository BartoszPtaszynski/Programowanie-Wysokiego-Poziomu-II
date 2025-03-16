class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"Pracuję jako {self.stanowisko}, zarabiam {self.pensja} zł"


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja, zespol_pracownikow):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol_pracownikow = zespol_pracownikow

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f", liczba podwładnych: {len(self.zespol_pracownikow)}"

    def dodaj_do_zespolu(self, pracownik: Pracownik):
        self.zespol_pracownikow.append(pracownik)


manager = Manager('Jan', 'Kowalski', 28, 'Manager', 20000, [])
pracownik1 = Pracownik('Michał', 'Nowak', 23, 'Software Developer', 14000)
pracownik2 = Pracownik('Jakub', 'Lok', 30, 'Software Developer IV', 15000)

manager.dodaj_do_zespolu(pracownik1)
manager.dodaj_do_zespolu(pracownik2)

print(manager.przedstaw_sie())
print(pracownik1.info_o_pracy())
print(pracownik2.info_o_pracy())
