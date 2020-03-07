def is_happy(n: int) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    while True:
        if n == 1:
            return True
        nums = sum([int(x)**2 for x in str(n)])
        if nums in seen:
            return False
        seen.add(nums)
        n = nums
