class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # Min must be in right half
                left = mid + 1
            else:
                # Min could be at mid or in left half
                right = mid

        return nums[left]
