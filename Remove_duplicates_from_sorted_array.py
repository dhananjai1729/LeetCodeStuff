class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        if len(nums) == 0:
            return j
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                j+=1
                nums[j] = nums[i]
        return j+1
