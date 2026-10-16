import pytest
from авл_дерево import ArbreAVL, NoeudAVL

def test_empty_and_single_node():
    avl = ArbreAVL()
    assert avl.get_hauteur(None) == 0
    assert avl.get_balance(None) == 0
    
    racine = NoeudAVL(10)
    assert avl.get_hauteur(racine) == 1
    assert avl.get_balance(racine) == 0

def test_rotation_droite_gauche_gauche():
    avl = ArbreAVL()
    racine = None
    # Insertion provoquant un déséquilibre Gauche-Gauche (Rotation Droite)
    racine = avl.insert(racine, 30)
    racine = avl.insert(racine, 20)
    racine = avl.insert(racine, 10)
    
    # Après rééquilibrage, 20 doit être la racine
    assert racine.valeur == 20
    assert racine.gauche.valeur == 10
    assert racine.droite.valeur == 30
    assert avl.get_hauteur(racine) == 2

def test_rotation_gauche_droite_droite():
    avl = ArbreAVL()
    racine = None
    # Insertion provoquant un déséquilibre Droite-Droite (Rotation Gauche)
    racine = avl.insert(racine, 10)
    racine = avl.insert(racine, 20)
    racine = avl.insert(racine, 30)
    
    assert racine.valeur == 20
    assert racine.gauche.valeur == 10
    assert racine.droite.valeur == 30

def test_double_rotation_gauche_droite():
    avl = ArbreAVL()
    racine = None
    # Déséquilibre Gauche-Droite
    racine = avl.insert(racine, 30)
    racine = avl.insert(racine, 10)
    racine = avl.insert(racine, 20)
    
    assert racine.valeur == 20
    assert racine.gauche.valeur == 10
    assert racine.droite.valeur == 30

def test_double_rotation_droite_gauche():
    avl = ArbreAVL()
    racine = None
    # Déséquilibre Droite-Gauche
    racine = avl.insert(racine, 10)
    racine = avl.insert(racine, 30)
    racine = avl.insert(racine, 20)
    
    assert racine.valeur == 20
    assert racine.gauche.valeur == 10
    assert racine.droite.valeur == 30
