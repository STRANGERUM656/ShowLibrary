class Libreria:
    def __init__(self):
        self.librerie = {}

    def aggiungi_libreria(self, nome, link):
        self.librerie[nome] = link

    def mostra_librerie(self):
        for nome, link in self.librerie.items():
            print(f"{nome}: {link}")

# Creazione di un'istanza della classe Libreria
mia_libreria = Libreria()

# Aggiunta di alcune librerie con i relativi link
mia_libreria.aggiungi_libreria("NumPy", "https://numpy.org/")
mia_libreria.aggiungi_libreria("Pandas", "https://pandas.pydata.org/")
mia_libreria.aggiungi_libreria("Matplotlib", "https://matplotlib.org/")
mia_libreria.aggiungi_libreria("Scikit-learn", "https://scikit-learn.org/")

# Mostra tutte le librerie con i relativi link
mia_libreria.mostra_librerie()
