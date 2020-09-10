from collections import defaultdict


def get_hint(secret: str, guess: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    h = defaultdict(int)
    bulls = cows = 0
    for idx, s in enumerate(secret):
        g = guess[idx]
        if s == g:
            bulls += 1
        else:
            cows += int(h[s] < 0) + int(h[g] > 0)
            h[s] += 1
            h[g] -= 1
    return "{}A{}B".format(bulls, cows)
