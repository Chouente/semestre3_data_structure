import pytest

from deque import ArrayDeque 

def test_initialization():
    d = ArrayDeque(5)
    assert d.is_empty() is True
    assert d.is_full() is False
    assert len(d) == 0
    assert d.to_list() == []

def test_add_and_remove_front():
    d = ArrayDeque(3)
    d.add_front(10)
    d.add_front(20)
    assert len(d) == 2
    assert d.to_list() == [20, 10]
    assert d.remove_front() == 20
    assert d.to_list() == [10]

def test_add_and_remove_back():
    d = ArrayDeque(3)
    d.add_back(10)
    d.add_back(20)
    assert d.to_list() == [10, 20]
    assert d.remove_back() == 20
    assert d.to_list() == [10]

def test_circular_behavior():
    d = ArrayDeque(3)
    d.add_back(1)
    d.add_back(2)
    d.remove_front()  # Libère l'espace au début
    d.add_back(3)     # Utilise la gestion circulaire
    assert d.to_list() == [2, 3]
    assert d.is_full() is False

def test_peek_functions():
    d = ArrayDeque(5)
    d.add_back(10)
    d.add_back(20)
    assert d.peek_front() == 10
    assert d.peek_back() == 20
    assert len(d) == 2  # Vérifie que peek ne retire rien

def test_search_and_contains():
    d = ArrayDeque(5)
    d.add_back(10)
    d.add_back(20)
    assert d.search(20) == 1
    assert d.search(99) == -1
    assert d.contains(10) is True
    assert d.contains(99) is False

def test_clear():
    d = ArrayDeque(5)
    d.add_back(10)
    d.clear()
    assert d.is_empty() is True
    assert d.to_list() == []

def test_exceptions():
    d = ArrayDeque(2)
    # Erreur sur deque vide
    with pytest.raises(IndexError, match="deque vide"):
        d.remove_front()
    with pytest.raises(IndexError, match="deque vide"):
        d.peek_back()
        
    # Erreur sur deque plein
    d.add_back(1)
    d.add_back(2)
    with pytest.raises(IndexError, match="deque plein"):
        d.add_front(3)
