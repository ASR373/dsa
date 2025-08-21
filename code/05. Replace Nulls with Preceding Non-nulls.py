
def replace_null_values(lst):
    for i in range(1, len(lst)):
        if lst[i] is None:
            lst[i] = lst[i-1]
    return lst
