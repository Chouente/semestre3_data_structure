def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # If no two elements were swapped by inner loop, then array is sorted
        if not swapped:
            break
            
    return arr
