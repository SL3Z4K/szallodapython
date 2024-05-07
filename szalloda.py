from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

        @abstractmethod
        def leiras(self):
            pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, meret):
        super().__init__(ar=45000, szobaszam=szobaszam)
        self.meret = meret

    def leiras(self):
        return f"Egyágyas szoba {self.szobaszam}-as sorszámmal. Az ára: {self.ar} Ft. egy éjszakára. Mérete: {self.meret}."

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, meret):
        super().__init__(ar=70000, szobaszam=szobaszam)
        self.meret = meret

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam}-as sorszámmal. Az ára: {self.ar} Ft. egy éjszakára. Mérete: {self.meret}."