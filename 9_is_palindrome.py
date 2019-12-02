def is_palindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome. An integer is a palindrome
    when it reads the same backward as forward.
    Coud you solve it without converting the integer to a string?
    """
    s = str(x)
    return s == s[::-1]


print(is_palindrome(121))  # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))  # False
print(is_palindrome(12344321))  # True
