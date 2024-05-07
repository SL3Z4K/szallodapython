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

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def szobak_szama(self):
        return len(self.szobak)



szalloda = Szalloda("Isten Király Hotel")
szalloda.add_szoba(EgyagyasSzoba(101, "Kicsi"))
szalloda.add_szoba(KetagyasSzoba(102, "Nagy"))

print(f"{szalloda.nev} szállodában összesen {szalloda.szobak_szama()} szoba van.")