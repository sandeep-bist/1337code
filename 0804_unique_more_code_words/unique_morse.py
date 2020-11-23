from typing import List


def uniqueMorseRepresentations(words: List[str]):
    """
    Time: O(s) where S is the sum of the length of words
    Space: O(s)
    """
    MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
             "....","..",".---","-.-",".-..","--","-.",
             "---",".--.","--.-",".-.","...","-","..-",
             "...-",".--","-..-","-.--","--.."]
    seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
            for word in words}
    return len(seen)
