def lengthOfLongestSubstring(s: str) -> int:
    """Solution to exercise 3 from leetcode.
    Return the lenght of the longest substring with only unique characters

    Constraints:
    s consists of English letters, digits, symbols and spaces.
    
    Args:
        s (str): String where to find the longest substring

    Returns:
        int: size of the longest substring without repeated characters
    """
    max_size = 0
    for i, c in enumerate(s):
        sub_str_chars = []
        sub_str_chars.append(c)
        for c2 in s[i + 1:]:
            if c2 in sub_str_chars:
                sub_str_size = len(sub_str_chars)
                max_size = sub_str_size if sub_str_size > max_size else max_size
                break
            sub_str_chars.append(c2)
        sub_str_size = len(sub_str_chars)
        max_size = sub_str_size if sub_str_size > max_size else max_size

    return max_size


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(" "))
