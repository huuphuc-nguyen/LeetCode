class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1 7 3  6  5  6 
        # left sum index:
        # 0 1 8  11 17 22

        # right summ index:
        #         11 5  0

        # create leftsum index array
        left = [0]

        for i in range (1, len(nums)):
            left.append(nums[i-1] + left[i-1])
        
        print(left)

        # create the right sum array
        right = [0] * len(nums)
        for i in range (len(nums) - 2,-1,-1):
            right[i] = (nums[i+1] + right[i+1])
        
        print(right)

        # find the index
        for i in range(len(left)):
            if left[i] == right[i]:
                return i
        
        return -1

        