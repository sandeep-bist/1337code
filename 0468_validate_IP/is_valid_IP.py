import re


def valid_IP_address(IP: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    if is_valid_IP4(IP):
        return "IPv4"
    if is_valid_IP6(IP):
        return "IPv6"
    return "Neither"


def is_valid_IP4(IP: str) -> bool:
    if IP.count('.') != 3:
        return False
    split = IP.split('.')
    if any(not x or
           not x.isdigit() or
           int(x) > 255 or
           (x[0] == "0" and len(x) > 1) for x in split):
        return False
    return True


def is_valid_IP6(IP: str) -> bool:
    if IP.count(':') != 7:
        return False
    split = IP.split(':')
    hexa = "0123456789ABCDEFabcdef"
    if any(not x or
           len(x) > 4 or
           any(c not in hexa for c in x) for x in split):
        return False
    return True


def is_valid_regex(IP: str) -> str:
    if re.search(r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$', IP):
        return 'IPv4'
    elif re.search(r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$', IP, re.I):
        return 'IPv6'
    return 'Neither'
