class NoeudListe:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None  # Pointeur vers le nœud suivant


class ListeChainee:
    def __init__(self):
        self.tete = None  # Premier élément de la liste

    def add(self, valeur):
        """Ajoute un élément à la fin de la liste (O(n))"""
        nouveau_noeud = NoeudListe(valeur)
        
        # Cas 1 : La liste est vide, le nouveau nœud devient la tête
        if self.tete is None:
            self.tete = nouveau_noeud
            return
            
        # Cas 2 : On parcourt la liste jusqu'au dernier nœud
        courant = self.tete
        while courant.suivant is not None:
            courant = courant.suivant
        
        # On accroche le nouveau nœud à la fin
        courant.suivant = nouveau_noeud

    def delete(self, valeur):
        """Supprime la première occurrence d'une valeur (O(n))"""
        if self.tete is None:
            return  # Liste vide, rien à faire

        # Cas particulier : L'élément à supprimer est la tête
        if self.tete.valeur == valeur:
            self.tete = self.tete.suivant
            return

        # Cas général : On cherche le nœud juste AVANT celui à supprimer
        courant = self.tete
        while courant.suivant is not None and courant.suivant.valeur != valeur:
            courant = courant.suivant

        # Si on a trouvé le nœud, on "saute" le nœud à supprimer en changeant le pointeur
        if courant.suivant is not None:
            courant.suivant = courant.suivant.suivant
