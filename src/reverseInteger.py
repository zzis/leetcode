import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        cache = x
        if x < 0:
            cache = -x
        newNum = '0'
        while cache != 0:
            newNum += str(cache % 10)
            cache /= 10
        newNum = int(newNum)
        if x < 0:
            newNum = -newNum
        if newNum > math.pow(2, 31) - 1 or newNum < -math.pow(2, 31):
            return 0
        return newNum

s = Solution()
print s.reverse(1534236469)