def to_goat_latin(S: str) -> str:
    """
    Time: O(n**2)
    Space: O(n**2)
    """
    split = S.split(" ")
    res = []
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 1
    for s in split:
        tmp = []
        if s[0].lower() in vowels:
            tmp.append(s)
        else:
            tmp.append(s[1:] + s[0])
        tmp.append("ma")
        tmp.append("a" * count)
        count += 1
        res.append("".join(tmp))
    return " ".join(res)
