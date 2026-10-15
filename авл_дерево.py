class NoeudAVL:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None
        self.hauteur = 1  # Un nouveau nœud est initialement à la hauteur 1


class ArbreAVL:
    def get_hauteur(self, noeud):
        if noeud is None:
            return 0
        return noeud.hauteur

    def get_balance(self, noeud):
        if noeud is None:
            return 0
        # Différence entre la hauteur de gauche et celle de droite
        return self.get_hauteur(noeud.gauche) - self.get_hauteur(noeud.droite)

    def rotation_droite(self, y):
        """Effectue une rotation vers la droite pour rééquilibrer"""
        x = y.gauche
        T2 = x.droite

        # Rotation des pointeurs
        x.droite = y
        y.gauche = T2

        # Mise à jour des hauteurs (on prend le max des enfants + 1)
        y.hauteur = 1 + max(self.get_hauteur(y.gauche), self.get_hauteur(y.droite))
        x.hauteur = 1 + max(self.get_hauteur(x.gauche), self.get_hauteur(x.droite))

        return x  # La nouvelle racine du sous-arbre

    def rotation_gauche(self, x):
        """Effectue une rotation vers la gauche pour rééquilibrer"""
        y = x.droite
        T2 = y.gauche

        # Rotation des pointeurs
        y.gauche = x
        x.droite = T2

        # Mise à jour des hauteurs
        x.hauteur = 1 + max(self.get_hauteur(x.gauche), self.get_hauteur(x.droite))
        y.hauteur = 1 + max(self.get_hauteur(y.gauche), self.get_hauteur(y.droite))

        return y  # La nouvelle racine du sous-arbre

    def insert(self, racine, valeur):
        """Insère une valeur de manière récursive puis rééquilibre (O(log n))"""
        # 1. Insertion classique dans un arbre binaire de recherche
        if racine is None:
            return NoeudAVL(valeur)

        if valeur < racine.valeur:
            racine.gauche = self.insert(racine.gauche, valeur)
        else:
            racine.droite = self.insert(racine.droite, valeur)

        # 2. Mettre à jour la hauteur du nœud parent
        racine.hauteur = 1 + max(self.get_hauteur(racine.gauche), self.get_hauteur(racine.droite))

        # 3. Calculer le facteur d'équilibre pour vérifier s'il est déséquilibré
        balance = self.get_balance(racine)

        # Cas 1 : Déséquilibre Gauche-Gauche (Rotation Droite)
        if balance > 1 and valeur < racine.gauche.valeur:
            return self.rotation_droite(racine)

        # Cas 2 : Déséquilibre Droite-Droite (Rotation Gauche)
        if balance < -1 and valeur > racine.droite.valeur:
            return self.rotation_gauche(racine)

        # Cas 3 : Déséquilibre Gauche-Droite (Rotation Gauche puis Droite)
        if balance > 1 and valeur > racine.gauche.valeur:
            racine.gauche = self.rotation_gauche(racine.gauche)
            return self.rotation_droite(racine)

        # Cas 4 : Déséquilibre Droite-Gauche (Rotation Droite puis Gauche)
        if balance < -1 and valeur < racine.droite.valeur:
            racine.droite = self.rotation_droite(racine.droite)
            return self.rotation_gauche(racine)

        return racine
