class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        def getIndices(rightShortArray, shortArray, longArray):
            midIndex = (len(shortArray) + len(longArray)) / 2
            rightLongArray = midIndex - rightShortArray
            return (rightShortArray - 1, rightShortArray, rightLongArray - 1, rightLongArray)
        
    
        def getDirection(leftShortArray, rightShortArray, leftLongArray, rightLongArray, shortArray, longArray):
            if getVal(shortArray, leftShortArray) > getVal(longArray, rightLongArray):
                return -1
            elif getVal(longArray, leftLongArray) > getVal(shortArray, rightShortArray):
                return 1
            else:
                return 0

        def getVal(array, i):
            if i == -1:
                return float('-inf')
            if i == len(array):
                return float('inf')
            return array[i]
        
        
        def getResult(leftShortArray, rightShortArray, leftLongArray, rightLongArray, shortArray, longArray):
            odd = (len(shortArray) + len(longArray)) % 2
            if odd:
                return min(getVal(longArray, rightLongArray), getVal(shortArray, rightShortArray))
            else:
                return (max(getVal(shortArray, leftShortArray), getVal(longArray, leftLongArray)) 
                        + min(getVal(shortArray, rightShortArray), getVal(longArray, rightLongArray))) / 2.0
        
        
        shortArray = nums1
        longArray = nums2
        if len(nums1) > len(nums2):
            shortArray = nums2
            longArray = nums1
            
        
        leftShortArray = rightShortArray = leftLongArray = rightLongArray = t = 1
            
         
        l = 0
        r = len(shortArray)
        while t != 0:
            m = (l + r) / 2
            
            leftShortArray, rightShortArray, leftLongArray, rightLongArray = getIndices(m, shortArray, longArray)
            
            t = getDirection(leftShortArray, rightShortArray, leftLongArray, rightLongArray, shortArray, longArray)
            if t < 0:
                r = m - 1
            elif t > 0:
                l = m + 1
        
        return getResult(leftShortArray, rightShortArray, leftLongArray, rightLongArray, shortArray, longArray)