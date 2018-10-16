class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLen = len(s)
        if strLen == 0:
            return ''
        start = 0
        length = 1
        longestLen = 1
        longestStr = ''
        dp = [[0 for i in range(strLen)] for i in range(strLen)]
        for i in range(strLen):
            dp[i][i] = 1
            if i < strLen - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                longestLen = 2
                longestStr = s[i: i + 2]
        for l in range(1, strLen + 1):
            print l
            for i in range(strLen):
                endPointer = i + l - 1
                if endPointer > strLen - 1:
                    break
                if i < strLen - 1 \
                    and dp[i + 1][endPointer - 1] == 1 \
                    and s[i] == s[endPointer]:
                    dp[i][endPointer] = 1
                    start = i
                    length = endPointer - i + 1
                    if longestLen < length:
                        longestLen = length
                        longestStr = s[start: endPointer + 1]
                    # print s[start: endPointer + 1]
                    # print i, endPointer
        if longestLen == 1:
            longestStr = s[0]
        # print dp
        return longestStr

# testStr = 'abccbbbccb'
# testStr = 'babad'
testStr = 'ccc'
s = Solution()
s.longestPalindrome(testStr)
print s.longestPalindrome(testStr)