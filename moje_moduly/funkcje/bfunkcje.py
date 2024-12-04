def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"Element listy {i+1} -> wartosc: {j}")

def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"Klucz: {x} -> wartosc: {y}")
