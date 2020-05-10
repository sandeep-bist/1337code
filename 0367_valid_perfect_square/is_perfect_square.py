def is_perfect_square(num: int) -> bool:
    """
    Time: O(log(n))
    Space: O(1)
    """
    if num < 2:
        return True
    left, right = 2, num // 2
    while left <= right:
        mid = (left + right) // 2
        squared = mid * mid
        if squared == num:
            return True
        if squared > num:
            right = mid - 1
        elif squared < num:
            left = mid + 1
    return False
