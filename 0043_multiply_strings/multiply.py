def multiply(num1: str, num2: str) -> str:
    """
    Time: O(n * m)
    Space: O(n + m)
    """
    res = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i + j + 1] += int(num1[i]) * int(num2[j])
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10
    i = 0
    while i < len(res) and res[i] == 0:
        i += 1
    res = ''.join([str(ele) for ele in res[i:]])
    return res if res else '0'