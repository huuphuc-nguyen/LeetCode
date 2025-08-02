class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [None] * len(nums)
        memo[-1] = nums[-1]
        memo[-2] = max(nums[-1], nums[-2])
        
        for i in range (len(nums) - 3, -1, -1):
            memo[i] = max(memo[i+1], memo[i+2] + nums[i])

        return memo[0]