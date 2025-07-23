class Solution:
    def findMin(self, nums: List[int]) -> int:
        def recursive(left, right):
            if left >= right:
                return min(nums[left], nums[right])

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                return recursive(mid + 1, right)
            else:
                return recursive(left, mid)

        return recursive(0, len(nums) - 1)
