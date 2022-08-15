def romanToInt(s: str) -> int:
    """This function solves exercise 13 of leetcode.
    It is meant to convert a string written in Roman Numerals to integer

    Args:
        s (str): roman numeral string

    Returns:
        int: roman numeral value in int
    """
    symbol_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    value = 0

    for i, symbol in enumerate(s):
        multiplier = 1
        # Treat special conditions where value needs to be subtracted
        # Instead of added
        # Change multiplier to reflect that
        if symbol == "I" and i < len(s) - 1:
            if s[i + 1] in ["V", "X"]:
                multiplier = -1
        elif symbol == "X" and i < len(s) - 1:
            if s[i + 1] in ["L", "C"]:
                multiplier = -1
        elif symbol == "C" and i < len(s) - 1:
            if s[i + 1] in ["D", "M"]:
                multiplier = -1

        value += symbol_to_value[symbol] * multiplier

    return value


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
