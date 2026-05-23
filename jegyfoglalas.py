class JegyFoglalas:
    def __init__(self, foglalas_id, jarat, utas_nev):
        self._foglalas_id = foglalas_id
        self._jarat = jarat
        self._utas_nev = utas_nev

    def get_id(self):
        return self._foglalas_id

    def __str__(self):
        return f"[{self._foglalas_id}] {self._utas_nev} - {self._jarat.get_jaratszam()} ({self._jarat.get_celallomas()})"