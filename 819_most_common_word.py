from collections import Counter
import re


def most_common_word(p, banned):
    """
    Given a paragraph and a list of banned words, return the most frequent
    word that is not in the list of banned words.  It is guaranteed there
    is at least one word that isn't banned, and that the answer is unique.
    Words in the list of banned words are given in lowercase, and free of
    punctuation.  Words in the paragraph are not case sensitive.  The
    answer is in lowercase.
    """
    s = set(banned)
    words = re.findall(r'\w+', p.lower())  # list of lower case words
    return Counter(w for w in words if w not in s).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(most_common_word(paragraph, ["hit"]))  # "ball"
