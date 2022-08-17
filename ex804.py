from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
    """Solution to exercise 804 of leetcode
    Receiving a list of words return the number of unique transformation 
    For when converted the words are converted to morse code.

    Args:
        words (List[str]): List of words to convert

    Contraints:
    All words are lowercase english letters

    Returns:
        int: total number of unique combination
    """
    char_to_morse = {
        'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--.."
    }
    transformations = set()
    for word in words:
        # iterate over every word
        in_morse = ""
        for c in word:
            # iterate over every character

            # add the character morse representation to
            # the word representation
            in_morse += char_to_morse[c]

        # let set handle repeated entries
        transformations.add(in_morse)

    # return total number of unique representations
    return len(transformations)


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
print(uniqueMorseRepresentations(["a"]))
