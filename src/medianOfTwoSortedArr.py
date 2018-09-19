class Solution(object):
    isLenOdd = False
    medianIndex = 0
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.medianIndex = (len(nums1) + len(nums2)) / 2
        self.isLenOdd = (len(nums1) + len(nums2)) % 2 == 1
        nums2Index = 0
        pointerIndex = 0
        lastItem = 0
        for i in range(len(nums1)):
            while nums2Index < len(nums2) and nums1[i] > nums2[nums2Index]:
                if pointerIndex == self.medianIndex:
                    return self.getMedianNum(lastItem, nums2[nums2Index])
                lastItem = nums2[nums2Index]
                nums2Index += 1
                pointerIndex += 1
            if pointerIndex == self.medianIndex:
                return self.getMedianNum(lastItem, nums1[i])
            lastItem = nums1[i]
            pointerIndex += 1
        for num2 in nums2[nums2Index:]:
            if pointerIndex == self.medianIndex:
                return self.getMedianNum(lastItem, num2)
            # lastItem = nums2[nums2Index]
            lastItem = num2
            pointerIndex += 1

    def getMedianNum(self, lastItem, currentItem):
        if self.isLenOdd:
            print 'medianIndex', self.medianIndex, 'medianValue', currentItem
            return currentItem
        else:
            print 'medianIndex', self.medianIndex, 'medianItem', lastItem, currentItem, 'medianValue', (currentItem + lastItem) / 2.0
            return (currentItem + lastItem) / 2.0


solution = Solution()
# solution.findMedianSortedArrays([1, 2, 7, 9, 11], [3, 4, 5, 6])
solution.findMedianSortedArrays([], [1, 2, 3, 4])
# solution.findMedianSortedArrays([1, 3], [2])