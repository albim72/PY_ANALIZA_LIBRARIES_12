class Book:
    #definicja stanu - konstrukotr klasy

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return (f"Książka -> {self.tytul}, autor: {self.autor}, cena: {self.cena}, okładka: {self.oprawa}")

    def __call__(self, message):
        print(f"ważna wiadomosc: {message}. Dotyczy książki: id-> {self.idbook}")

    def create_book(self):
        print("Uworzono obiekt klasy Book! (nową książkę!)")


#tworzenie obiektu
bk1 = Book(26,"Poradnik początkującego kulturysty","Michał Stec",42)
print(bk1)
bk1("tylko miękka oprawa!")

