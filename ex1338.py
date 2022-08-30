from collections import OrderedDict
from typing import Counter, List


def minSetSize(arr: List[int]) -> int:
    """Solution to exercise 1338 from leetcode.
    Given a integer array return the minimun size of a set that when all copies
    of the elements of the set are removed the lenght of the array is smaller than
    haft is original size.
    
    Args:
        arr (List[int]): Array of integers to check.
    
    Constraint:
        arr.length is even.

    Returns:
        int: size of the chosen set.
    """
    counts = OrderedDict(Counter(arr).most_common())
    set_size = 0
    total_len = 0
    for nc in counts.values():
        total_len += nc
        set_size += 1
        if total_len >= len(arr) / 2:
            return set_size


print(minSetSize([5, 5, 5, 2, 2, 7, 3, 3, 3, 3]))
print(minSetSize([7, 7, 7, 7, 7, 7]))
print(minSetSize([9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58,
                  19]))
