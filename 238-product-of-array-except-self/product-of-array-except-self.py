class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   1         2           3          4 
    #result: 2 3 4     1 3 4       1 2 4      1 2 3 

    #preifx:  1           1         1 2       1 2 3
    #suffix: 1 2 3 4     3 4        4          1

        # prefix= [0] * len(nums)
        # suffix= [0] * len(nums)
        # prefix[0] = 1
        # suffix[len(nums)-1]=1
        # for i in range(1, len(nums)):
        #     prefix[i] = nums[i-1] * prefix[i-1]
        # for i in range(len(nums)-2,-1,-1):
        #     suffix[i] = nums[i+1] * suffix[i+1]

        # return [a * b for a, b in zip(prefix, suffix)]

        # Followup: utilize prefix as the return array, use 1 variable to keep track suffix sum
        
        n = len(nums)
        result = [1] * n  # This will act as the "prefix" array
        
        # Step 1: Calculate the prefix products and store in result
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Step 2: Calculate the suffix product while updating the result
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

