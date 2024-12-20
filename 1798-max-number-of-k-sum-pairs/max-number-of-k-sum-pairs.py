class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1 3 3 3 4
        #   l   r   
        # sum is < k -> increase left  


        nums = sorted(nums)
        l = 0
        r = len(nums) - 1
        op = 0

        while l < r:
            sum = nums[l] + nums[r]
            if sum < k:
                l += 1
            elif sum > k:
                r -= 1
            else:
                op += 1
                l+=1
                r-=1
        
        return op
