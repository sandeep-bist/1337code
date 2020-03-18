def defang_IP_addr(address: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    return address.replace(".", "[.]")
