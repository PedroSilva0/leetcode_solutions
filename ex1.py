from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """Solution to ex1 of leetcode
    Given a list of numbers return a list with the indices of the two numbers 
    that when added together result in the target number.
    
    Contraints:
    Only one valid answer exists 
    You may not use the same element twice.

    Args:
        nums (List[int]): List of numbers
        target (int): targed number

    Returns:
        List[int]: list with the two numbers that when summed result in target
    """
    for i, n in enumerate(nums[:-1]):
        if target - n in nums[i + 1:]:
            # The number we need is in a part of the list we did not check yet

            # the index is relative to the sliced list so we
            # need to add both the current index + 1 to get
            # the original list index
            return [i, nums[i + 1:].index(target - n) + i + 1]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
