def calculate(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    s += '+0'
    stack, num, last_op = [], 0, "+"
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif not c.isspace():
            if last_op == "-":
                stack.append(-num)
            elif last_op == "+":
                stack.append(num)
            elif last_op == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            last_op, num = c, 0
    return sum(stack)