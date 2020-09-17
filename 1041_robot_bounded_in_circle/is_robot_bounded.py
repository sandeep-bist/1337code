def is_robot_bounded(instructions: str) -> bool:
    """
    Time: O(n)
    Space: O(1)
    """
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    x = y = d = 0
    for c in instructions:
        if c == 'L':
            d = (d + 3) % 4
        elif c == 'R':
            d = (d + 1) % 4
        else:
            x, y = x + dirs[d][0], y + dirs[d][1]
    return (not x and not y) or d
