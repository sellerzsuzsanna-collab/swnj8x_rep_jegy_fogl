from legitarsasag import LegiTarsasag
from belfoldi import BelfoldiJarat
from nemzetkozi import NemzetkoziJarat

def alap_adatok_feltoltese():
    lt = LegiTarsasag("SelZsu")

    bfj1 = BelfoldiJarat("BF134", "Sopron", 21300)
    bfj2 = BelfoldiJarat("BF244", "Miskolc", 34000)
    nkj3 = NemzetkoziJarat("NK278", "London", 87600)

    lt.hozzaad_jarat(bfj1)
    lt.hozzaad_jarat(bfj2)
    lt.hozzaad_jarat(nkj3)

    # 6 előre foglalás
    lt.foglal("BF134", "Kiss János")
    lt.foglal("BF134", "Nagy Anna")
    lt.foglal("BF244", "Tóth Béla")
    lt.foglal("BF244", "Szabó Éva")
    lt.foglal("NK278", "Kovács Péter")
    lt.foglal("NK278", "Varga Lili")

    return lt

def felhasznaloi_menu():
    lt = alap_adatok_feltoltese()

    while True:
        print("\n--- Repülőjegy Foglalás ---")
        print("1 - Járatok listázása")
        print("2 - Foglalások listázása")
        print("3 - Jegy foglalása")
        print("4 - Foglalás lemondása")
        print("0 - Kilépés")

        valasz = input("Választás: ")

        try:
            if valasz == "1":
                lt.listaz_jaratok()

            elif valasz == "2":
                lt.listaz_foglalasok()

            elif valasz == "3":
                jaratszam = input("Járatszám: ")
                nev = input("Név: ")
                ar = lt.foglal(jaratszam, nev)
                print(f"Sikeres foglalás! Ár: {ar} Ft")

            elif valasz == "4":
                fid = int(input("Foglalás ID: "))
                lt.lemond(fid)
                print("Foglalás lemondva.")

            elif valasz == "0":
                print("Kilépés...")
                break

            else:
                print("Érvénytelen választás!")

        except Exception as e:
            print("Hiba:", e)
