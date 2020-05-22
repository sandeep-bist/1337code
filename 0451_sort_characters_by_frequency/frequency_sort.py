from collections import Counter


def frequency_sort(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    return ("".join(char * times for char, times in Counter(s).most_common()))


def frequency_sort_bucket(s: str) -> str:
    """
    Time: O(n)
    Space: O(n)
    """
    buckets, res = [[]]*len(s), ""
    counter = Counter(s)
    for ch, cnt in counter.items():
        buckets[cnt-1] = buckets[cnt-1]+[ch]
    for i in range(len(buckets)-1, -1, -1):
        if buckets[i]:
            res += "".join([c*(i+1) for c in buckets[i]])
    return res
