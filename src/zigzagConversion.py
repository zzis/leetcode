class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        split = numRows * 2 - 3
        cycle = split
        result = ''
        start = 0
        while start < numRows:
            pointer = start
            nextSplit = split
            while pointer < len(s):
                result += s[pointer]
                pointer += nextSplit
                if nextSplit != split:
                    nextSplit = cycle % split
                if nextSplit == 1:
                    nextSplit = cycle
            split -= 2
            start += 1
        return result


s = Solution()
inputStr = 'PAYPALISHIRING'
lineNumber = 4
result = 'PINALSIGYAHRPI'
print inputStr
print s.convert(inputStr, lineNumber)
print s.convert(inputStr, lineNumber) == result