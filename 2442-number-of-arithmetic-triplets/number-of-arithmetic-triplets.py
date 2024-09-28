class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        result = 0

        for i in range(0,len(nums)-1,1): 
            number_next = nums[i] + diff 
            number_next_next = nums[i] + diff + diff

            if (number_next in nums) and (number_next_next in nums):
                result += 1

        return result