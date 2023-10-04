def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return ("Seda numbrit ei ole listis")
    
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    
    elif target < l[midpoint]:
        new_high = midpoint - 1
        return binary_search(l, target, low, new_high) 
    
    else:
        new_low = midpoint + 1
        return binary_search(l, target, new_low, high)
    

l = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 7
print(binary_search(l, target))