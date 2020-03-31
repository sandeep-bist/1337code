def reverse_str(s: str, k: int) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    arr = list(s)
    for i in range(0, len(arr), k * 2):
        arr[i: i + k] = arr[i: i + k][::-1]
    return "".join(arr)
