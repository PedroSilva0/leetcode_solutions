# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode],
                  l2: Optional[ListNode]) -> Optional[ListNode]:
    """Solution to exercise 2 from leetcode.
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Constraints:
    It is guaranteed that the list represents a number that does not have leading zeros.

    Args:
        l1 (Optional[ListNode]): _description_
        l2 (Optional[ListNode]): _description_

    Returns:
        Optional[ListNode]: _description_
    """
    l1_value = list_node_to_int(l1)
    l2_value = list_node_to_int(l2)

    total = l1_value + l2_value

    return int_to_list_node(total)


def list_node_to_int(l: ListNode) -> int:
    """This function converts a ListNode to its integer value.

    Args:
        l (ListNode): List node to convert

    Returns:
        int: integer value of the received list node
    """
    l_str: str = str(l.val)

    next_node: ListNode = l.next
    while next_node:
        l_str.append(str(next_node.val))
        next_node = next_node.next

    # Reverse the string and convert to int
    return int(l_str[::-1])


def int_to_list_node(value: int) -> ListNode:
    """This function converts a integer to its equivalent representation in a ListNode.
    Keep in mind the list node is meant to be reversed.

    Args:
        value (int): value to convert to ListNode

    Returns:
        ListNode: ListNode representation of the received integer
    """
    # Convert to string and reverse it

    value_str: str = str(value)[::-1]

    # Keep the start pointer
    start: ListNode = ListNode(value_str[0])
    prev: ListNode = start

    # If len of the value in string is only one digit we are done
    if len(value_str) > 1:
        # Multi digit value construct the ListNode by linking the
        # previously initiated node to the newly created one
        for c in value_str[1:]:
            l: ListNode = ListNode(c)
            if prev:
                prev.next = l
            prev = l

    return start
