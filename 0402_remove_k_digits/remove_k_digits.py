def remove_k_digits(num: str, k: int) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    num_stack = []
    for n in num:
        while k and num_stack and num_stack[-1] > n:
            num_stack.pop()
            k -= 1
        num_stack.append(n)
    final = num_stack[:-k] if k else num_stack
    return "".join(final).lstrip("0") or "0"
