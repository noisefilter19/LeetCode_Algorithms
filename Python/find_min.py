class Solution(object):
    def findMin(self, nums):
        if nums is None or len(nums)==0:
            return None
        m = nums[0]
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            m = min(m, nums[l], nums[p], nums[r])

            if nums[l]<nums[r]:
                break
            elif nums[l]<nums[p]:
                l = p+1
            elif nums[p]<nums[r]:
                r = p-1
            else:
                l = l+1
                r = r-1
        return m