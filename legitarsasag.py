from jegyfoglalas import JegyFoglalas as jf

class LegiTarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []
        self._kov_id = 1

    def hozzaad_jarat(self, jarat):
        self._jaratok.append(jarat)

    def listaz_jaratok(self):
        for j in self._jaratok:
            print(f"{j.get_jaratszam()} - {j.get_celallomas()} - {j.get_jegyar()} Ft ({j.tipus()})")

    def foglal(self, jaratszam, utas_nev):
        try:
            jarat = next(j for j in self._jaratok if j.get_jaratszam() == jaratszam)
        except StopIteration:
            raise Exception("Nincs ilyen járat!")

        foglalas = jf(self._kov_id, jarat, utas_nev)
        self._foglalasok.append(foglalas)
        self._kov_id += 1

        return jarat.get_jegyar()
    
    def lemond(self, foglalas_id):
        for f in self._foglalasok:
            if f.get_id() == foglalas_id:
                self._foglalasok.remove(f)
                return True
        raise Exception("Foglalás nem található!")

    def listaz_foglalasok(self):
        if not self._foglalasok:
            print("Nincsenek foglalások.")
        for f in self._foglalasok:
            print(f)