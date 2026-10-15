class масиф:
    def __init__(self):
        self.capacite = 4
        self.size = 0
        self.tab = [None]*self.capacite
        
    def add(self, nber):
        if self.capacite == self.size:
            self._redimensionner()
        self.tab[self.size] = nber
        self.size += 1
        
    def redimensionner(self):
        print("your table is...")
        self.capacite = self.capacite * 2
        new_table = [None] * self.capacite
        
        for i in range(self.size):
            new_table[i] = self.tab[i]
        self.tab = new_table
        
    def delete(self, nber):
        indice_trouve = -1
        
        # ÉTAPE 1 : Trouver l'indice de l'élément dans le tableau
        for i in range(self.size):
            if self.tab[i] == nber:
                indice_trouve = i
                break # On a trouvé l'élément, on arrête la recherche
        
        # Si l'élément n'est pas dans le tableau, on ne fait rien
        if indice_trouve == -1:
            print(f"L'élément {nber} n'existe pas dans le tableau.")
            return

        # ÉTAPE 2 : Décaler tous les éléments suivants d'une case vers la gauche
        for i in range(indice_trouve, self.size - 1):
            self.tab[i] = self.tab[i + 1]
            
        # ÉTAPE 3 : Nettoyer la dernière case devenue doublon et réduire la taille
        self.tab[self.size - 1] = None
        self.size -= 1
