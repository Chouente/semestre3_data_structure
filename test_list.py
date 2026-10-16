import pytest
from Лист import ListeChainee

def helper_to_list(liste_chainee):
    res = []
    courant = liste_chainee.tete
    while courant:
        res.append(courant.valeur)
        courant = courant.suivant
    return res

def test_add_elements():
    liste = ListeChainee()
    assert liste.tete is None
    
    liste.add(5)
    assert liste.tete.valeur == 5
    
    liste.add(10)
    liste.add(15)
    assert helper_to_list(liste) == [5, 10, 15]

def test_delete_head():
    liste = ListeChainee()
    liste.add(1)
    liste.add(2)
    
    liste.delete(1)  # Supprime la tête
    assert helper_to_list(liste) == [2]

def test_delete_middle_or_end():
    liste = ListeChainee()
    liste.add(10)
    liste.add(20)
    liste.add(30)
    
    liste.delete(20)  # Supprime au milieu
    assert helper_to_list(liste) == [10, 30]
    
    liste.delete(30)  # Supprime la fin
    assert helper_to_list(liste) == [10]

def test_delete_non_existent_and_empty():
    liste = ListeChainee()
    # Sur liste vide, ne doit pas planter
    liste.delete(5) 
    
    liste.add(10)
    liste.delete(99)  # Valeur inexistante
    assert helper_to_list(liste) == [10]
