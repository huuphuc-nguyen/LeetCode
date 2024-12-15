class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
       
       #20 100 10 101 5 101
        
# Keep track of two variables (first and second) to represent the first and second smallest elements seen so far.
# Loop through the array and try to find the third element.
# If the current number is smaller than first, update first.
# Else, if the current number is between first and second, update second.
# If the current number is greater than second, then a valid triplet 
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

