def find_target(root, k):
    """
    Time: O(n)
    Space: O(n)
    """
    if not root:
        return False
    return find(root, set(), k)

def find(root, seen, k):
    if not root:
        return False
    compliment = k - root.val
    if compliment in seen:
        return True
    seen.add(root.val)
    return find(root.left, seen, k) or find(root.right, seen, k)
