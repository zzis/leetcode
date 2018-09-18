def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    cache = dict()
    length = 0
    longest = 0
    head = 0
    tail = 0
    for index, ch in enumerate(s):
        tail += 1
        if ch in cache and head <= cache[ch]:
            head = cache[ch] + 1
        cache[ch] = index
        length = tail - head
        print 'head', head, 'tail', tail, 'length', length, 'cache', cache
        if length > longest:
            longest = length
    return longest

print lengthOfLongestSubstring('aabaab!bb')