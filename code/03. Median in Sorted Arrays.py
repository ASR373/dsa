import math
def find_median_sorted_arrays(input):
    """ 
    :type input: Dict[str, List[int]]
    :rtype: float
    """

    nums1 = input["nums1"]
    nums2 = input["nums2"]
    nums1 = nums1 + nums2
    
    def qs(arr):
        length = len(arr)
        if length <= 1:
            return arr
        else:
            pivot = arr.pop()
        
        items_greater = []
        items_lower = []
        
        for item in arr:
            if item >pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        
        return qs(items_lower) + [pivot] + qs(items_greater)
        
    nums1 = qs(nums1)
    length = len(nums1)
    if length % 2 == 0:
        return (nums1[math.floor(length/2) - 1] + nums1[math.ceil(length/2)])/2
    else:
        return nums1[length//2]
