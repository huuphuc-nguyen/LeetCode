class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   1         2           3          4 
    #result: 2 3 4     1 3 4       1 2 4      1 2 3 

    #preifx:  1           1          1 2       1 2 3
    #suffix: 1 2 3 4     3 4        4          1

        prefix= [0] * len(nums)
        suffix= [0] * len(nums)
        prefix[0] = 1
        suffix[len(nums)-1]=1
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]

        return [a * b for a, b in zip(prefix, suffix)]
