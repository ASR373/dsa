def qs(arr, k):
    
    if len(arr) < k:
        print("insufficient elements")
        return None

    k = len(arr) - k
    pivot = arr[-1]


    left = []
    right = []
    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    
    new_array = left + [pivot] + right
    if len(left) == k:
        return pivot
    elif len(left) > k:
        return qs(left, k)
    else:
        return qs(right, k - len(left) - 1)
    return pivot

print(qs([3, 2, 1, 5, 4], 2))  # Output: 4


# mothala lenth of the array paakanum insufficient naa vitru
# since largest thedurathu naala kth largest is len(Arr)-k
# pivot last element
# left and right eduthuko
# new array create pannu
#left side oda length = k naa return pivot... len(left) > k naa left side la thirumba func run pannu if not right la run pannu with k - len(left) - 1

