def num_squares(n: int) -> int:
    """
    Time: O(n * h/2) where h is the height of the N-ary tree
    Space: O(sqrt(n) * h)
    """
    if n < 2:
        return n
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1
    count = 0
    q = {n}
    while q:
        count += 1
        s = set()
        for x in q:
            for y in squares:
                if x == y:
                    return count
                if x < y:
                    break
                s.add(x-y)
        q = s
    return count
