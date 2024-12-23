class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 1 1 1 1   k = 3
        #         

        # 1 1 1 0 0 0 1 1 1 1 0
        #          s           x

        maxC = 0
        count = 0
        start = 0

        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] == 0:
                k -= 1
            count += 1
            

        maxC = count 

        for i in range (count, len(nums)):
            if nums[i] == 1:
                count += 1
                maxC = max(maxC, count)
            else:
                if nums[start] == 0:
                    start += 1
                    continue
                else:
                    while nums[start] != 0:
                        start += 1
                        count -= 1
                    start += 1
                    continue
        
        return maxC


    

