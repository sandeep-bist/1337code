from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    s = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        s.add(local + "@" + domain)
    return len(s)