# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


def rand10() -> int:
    """
    Time: O(1) - O(infinity)
    Space: O(1)
    """
    rand40 = 40
    while rand40 >= 40:
        rand40 = (rand7() - 1) * 7 + rand7() - 1
    return rand40 % 10 + 1
