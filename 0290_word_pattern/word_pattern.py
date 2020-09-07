def word_pattern(pattern: str, str: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    split = str.split(" ")
    if len(split) != len(pattern):
        return False
    d = {}
    for i in range(len(pattern)):
        c = "c_" + pattern[i]
        w = "w_" + split[i]
        if c not in d:
            d[c] = i
        if w not in d:
            d[w] = i
        if d[c] != d[w]:
            return False
    return True
