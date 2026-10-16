import pytest 
from bubble_sort import bubble_sort

def test_bubble_sort_standard():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_bubble_sort_already_sorted():
    # Teste le mécanisme d'arrêt précoce (si la liste est déjà triée)
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_bubble_sort_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_bubble_sort_duplicates():
    assert bubble_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]

def test_bubble_sort_empty_and_single():
    assert bubble_sort([]) == []
    assert bubble_sort([42]) == [42]

def test_bubble_sort_negative_numbers():
    assert bubble_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3]
