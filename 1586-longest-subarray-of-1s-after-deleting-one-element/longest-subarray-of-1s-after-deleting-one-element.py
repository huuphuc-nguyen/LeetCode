class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 0 1 1 1 0 1 1 0 1 
        #           s   x

        # count = 6
        # available = 0


        available = 1
        start = 0
        count = 0
        maxCount = 0

        # initalize the window
        for i in range(len(nums)):
            if available <= 0:
                break
            if nums[i] == 0:
                available -=1
            count += 1
        
        # initialize the max
        maxCount = count

        # slide the window
        for i in range(count, len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount, count)
                continue
            if nums[i] == 0:
                while nums[start] != 0:
                    start += 1
                    count -= 1
                start += 1
                continue
        
        return maxCount - 1

