class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Add new element, remove old element
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is larger
            
        return max_sum / k