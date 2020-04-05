def climb_stairs(n: int) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    memo = {}
    return helper(n, 0, memo)


def helper(n: int, curr: int, memo) -> int:
    if curr > n:
        return 0
    if curr == n:
        return 1
    if curr in memo:
        return memo[curr]
    memo[curr] = helper(n, curr + 1, memo) + helper(n, curr + 2, memo)
    return memo[curr]
