class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newset = set(nums)
        if len(newset) < len(nums):
            return True
        return False