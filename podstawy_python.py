print("kolekcje języka pyhton!")

a: int = 700
print(a)
print(type(a))

a = "siedem"
print(a)
print(type(a))

#kolekcje w pythonie -> lista, krotka, zbiór i słownik

"""
komentarz wieloliniowy
"""

#lista
cyfry = [3,5,2,6,7,2,5,7,8,3,2,5]
imiona = ("Jan","Maria","Tomasz","Jan","Ula")
print(cyfry)
print(type(cyfry))

print(imiona)
print(type(imiona))

cyfry.append(1)
print(cyfry)

cyfry.remove(3)
print(cyfry)

cyfry.sort()
print(cyfry)
cyfry.sort(reverse=True)
print(cyfry)

print(cyfry[0])
print(cyfry[3])

print(cyfry[1:4])

print(cyfry[-1])
print(cyfry[2:])
print(cyfry[:3])

print(imiona[2])
print(imiona[2:4])

cyfry[1:4] = [5,2,5,2,5,7,8,3,2]
print(cyfry)

# imiona[1:4] = ["Lara","Leon",]

imiona = list(imiona)
imiona.extend(["Ilona","Olaf","Nadia"])
print(imiona)

imiona = tuple(imiona)
print(imiona)
#zbiór

kolory ={"niebieski","czerwony","zielony","fioletowy","biały","zielony"}
print(kolory)

kolory.add("magenta")
print(kolory)

kolory.update(["złoty","zółty","szmaragdowy"])
print(kolory)

kolory.add("czerwony")
print(kolory)

kolory.remove("złoty")
print(kolory)

kolory.discard("łososiowy")
print(kolory)

kolory.discard("biały")
print(kolory)

s = "pralnia chemiczna"

print(s)
print(s[0])
print(s[1])
print(s[2:5])

info = ["specjalna opcja","inna opcja"]
print(info)
print(info[0])
print(info[0][2])

#słownik
osoba = {
    "imię":"Jan",
    "nazwisko":"Nowak",
    "miasto":"Kraków",
    "wiek":43
}
print(osoba)

print(osoba["imię"])
osoba["dni"]  =  11
print(osoba)

osoba["wiek"] = 50

print(osoba)

print(osoba.keys())
print(osoba.values())

osoba["Wiek"] = 80

print(osoba)

spis = {
    
    "osoba1":{
    "imię":"Jan",
    "nazwisko":"Nowak",
    "miasto":"Kraków",
    "wiek":43
    },
    "osoba2": {
        "imię": "Anna",
        "nazwisko": "Nowak",
        "miasto": "Kraków",
        "wiek": 43
    }
}
