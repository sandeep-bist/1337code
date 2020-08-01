def detect_capital_use(word: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    uppers = sum(x.isupper() for x in word)
    if uppers == 1:
        return word[0].isupper()
    return not uppers or uppers == len(word)


def detect_capital_built_ins(word):
    return word.isupper() or word.islower() or word.istitle()
