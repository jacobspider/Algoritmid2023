function ternarySearch(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = mid1 + (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternarySearch(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternarySearch(arr, mid2 + 1, right, key)
        else:
            return ternarySearch(arr, mid1 + 1, mid2 - 1, key)
    
    return -1  # Element not found
