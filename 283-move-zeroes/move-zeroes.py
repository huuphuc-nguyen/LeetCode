class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 0 1 0 3 12
        # 1 3 12 0 0    
        #   l    r   

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == 0:
                # # shift the array
                # 0 1 0 3 12
                # l        r
                for i in range(left, right):
                    nums[i] = nums[i+1]
                # assigned 0 to right pointer
                nums[right] = 0
                # decrease right pointer
                right -= 1
            if nums[left] != 0:
                left += 1
    