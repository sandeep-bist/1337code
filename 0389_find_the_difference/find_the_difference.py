def find_the_difference(s: str, t: str) -> str:
    """
    Time: O(n)
    Space: O(1)
    """
    num = 0
    for char in t:
        num += ord(char)
    for char in s:
        num -= ord(char)
    return chr(num)
