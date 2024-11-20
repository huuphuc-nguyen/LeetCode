class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0


        for num in num_set:
            if num - 1 not in num_set:
                lookup = num+1
                current_streak = 1

                while lookup in num_set:
                    lookup+=1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest

        
            


        