import pytest
from масив import масиф

def test_initial_state():
    m = масиф()
    assert m.capacite == 4
    assert m.size == 0
    assert m.tab == [None, None, None, None]

def test_add_without_resize():
    m = масиф()
    m.add(10)
    m.add(20)
    assert m.size == 2
    assert m.tab[0] == 10
    assert m.tab[1] == 20

def test_auto_resize():
    m = масиф()
    # Remplissage jusqu'à la capacité max initiale (4)
    m.add(1)
    m.add(2)
    m.add(3)
    m.add(4)
    
    # Le 5ème élément doit déclencher le redimensionnement automatique
    m.add(5) 
    assert m.capacite == 8
    assert m.size == 5
    assert m.tab[:5] == [1, 2, 3, 4, 5]

def test_delete_existing_element():
    m = масиф()
    m.add(10)
    m.add(20)
    m.add(30)
    
    m.delete(20)  # Doit décaler 30 vers la gauche
    assert m.size == 2
    assert m.tab[0] == 10
    assert m.tab[1] == 30
    assert m.tab[2] is None  # Nettoyage de la case doublon

def test_delete_non_existing_element(capsys):
    m = масиф()
    m.add(10)
    m.delete(99)
    
    # Vérifie que la taille n'a pas bougé
    assert m.size == 1
    # Vérifie le message d'erreur dans la console
    captured = capsys.readouterr()
    assert "L'élément 99 n'existe pas" in captured.out
