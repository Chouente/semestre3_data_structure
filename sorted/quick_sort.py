def quick_sort(arr):
    """Sorts an array recursively using the Quick Sort algorithm (O(n log n))"""
    # Base Case: Array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr
    
    # Selecting the pivot element (using the last item here)
    pivot = arr[-1]
    
    # Sub-array generation via comprehension strategies
    # left: elements smaller than or equal to pivot (excluding the pivot itself)
    left = [x for x in arr[:-1] if x <= pivot]
    
    # right: elements strictly greater than pivot
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursive step: sort sub-segments and concatenate around pivot marker
    return quick_sort(left) + [pivot] + quick_sort(right)
