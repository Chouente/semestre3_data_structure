import pytest
from quick_sort import quick_sort

def test_quick_sort_standard():
    assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_quick_sort_already_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quick_sort_duplicates():
    assert quick_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]

def test_quick_sort_empty_and_single():
    # Valide le cas de base de la récursion (len <= 1)
    assert quick_sort([]) == []
    assert quick_sort([42]) == [42]

def test_quick_sort_negative_numbers():
    assert quick_sort([3, -1, 2, -5, 0]) == [-5, -1, 0, 2, 3]
