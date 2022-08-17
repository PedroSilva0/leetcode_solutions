def firstUniqChar(s: str) -> int:
    """Solution to exercise 387 from leetcode.
    Return the index of the first non repeating character
    if it does not exist return -1.
    
    Constraints:
    s consists of only lowercase English letters.

    Args:
        s (str): string to check for the unique element

    Returns:
        int: index of the first unique element
    """
    ocurrences = {}

    for i, c in enumerate(s):
        if c in ocurrences:
            ocurrences[c]['n'] += 1
            continue
        ocurrences[c] = {}
        ocurrences[c]["n"] = 1
        ocurrences[c]["index"] = i

    index = len(s)
    for value in ocurrences.values():
        if value["n"] == 1 and value['index'] < index:
            index = value['index']

    if index == len(s):
        return -1

    return index


print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
print(firstUniqChar("dddccdbba"))
