Given a list of values containing NULLs, for every null value, replace it with its preceding non-null value.

Constraints
The input variable lst is a list.
The elements of lst can be either integers or None.
The length of lst can be any positive integer.
The list lst may contain multiple consecutive None values.
The list lst may start with a None value.
The list lst may end with a None value.


sol:


def replace_null_values(lst):
    for i in range(1, len(lst)):
        if lst[i] is None:
            lst[i] = lst[i-1]
    return lst
