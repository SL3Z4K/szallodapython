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

    def __repr__(self):
        return f"Egyágyas szoba(szobaszám={self.szobaszam}, méret='{self.meret}')"


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, meret):
        super().__init__(ar=70000, szobaszam=szobaszam)
        self.meret = meret

    def leiras(self):
        return f"Kétágyas szoba {self.szobaszam}-as sorszámmal. Az ára: {self.ar} Ft. egy éjszakára. Mérete: {self.meret}."

    def __repr__(self):
        return f"Kétágyas szoba(szobaszam={self.szobaszam}, méret='{self.meret}')"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def szobak_szama(self):
        return len(self.szobak)

    def szoba_foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas.szoba.ar
        return None

    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Foglalások: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __repr__(self):
        return f"Foglalt szoba: {self.szoba}, dátum:{self.datum}"


def main():
    szalloda = Szalloda("Isten Király Hotel")
    szalloda.add_szoba(EgyagyasSzoba(101, "Kicsi"))
    szalloda.add_szoba(KetagyasSzoba(102, "Nagy"))
    szalloda.add_szoba(EgyagyasSzoba(103, "Kicsi"))

    while True:
        print("\nVálasszon műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Fgolalások listázása")
        print("4. Kilépés")

        valasztas = input("Kérem válasszon:")

        if valasztas == "1":
            szobaszam = int(input("Kérem adja meg a szoba számát: "))
            datum = input("Kérem adja meg a foglalás dátumát:")
            szalloda.szoba_foglalas(szobaszam, datum)
            print("Foglalás sikeren rögzítve!")

        elif valasztas == "2":
            szobaszam = int(input("Kérem adja meg a szoba sorszámát: "))
            datum = input("Kérem adja meg a foglalás dátumát: ")
            if szalloda.foglalas_lemondas(szobaszam, datum):
                print("A foglalását sikeresen lemondta!")
            else:
                print("Nem található ilyen foglalás.")

        elif valasztas == "3":
            szalloda.foglalasok_listazasa()

        elif valasztas == "4":
            print("Kilépés")
            break

        else:
            print("Ez az opció nem elérhető, kérem válasszon újra!")


szalloda = Szalloda("Isten Király Hotel")
szalloda.add_szoba(EgyagyasSzoba(101, "Kicsi"))
szalloda.add_szoba(KetagyasSzoba(102, "Nagy"))
szalloda.add_szoba(EgyagyasSzoba(103, "Kicsi"))

foglalas1 = szalloda.szoba_foglalas(101, "2024-06-23")
foglalas2 = szalloda.szoba_foglalas(102, "2024-07-25")
foglalas3 = szalloda.szoba_foglalas(101, "2024-07-26")

#szalloda.foglalas_lemondas(101, "2024-06-23")
szalloda.foglalas_lemondas(102, "2024-07-25")

print(f"{szalloda.nev} szállodában összesen {szalloda.szobak_szama()} szoba van.")

print(foglalas1)
print(foglalas2)

print(szalloda.foglalasok)

szalloda.foglalasok_listazasa()

if __name__ == "__main__":
    main()
