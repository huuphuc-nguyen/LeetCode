class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        maxC = 0  
        count = 0  
        start = 0  # Pointer to mark the start of the sliding window.

        # First loop to calculate the initial window size based on `k`.
        for i in range(len(nums)):
            if k == 0:  # If no flips are remaining, stop expanding the initial window.
                break
            if nums[i] == 0:  # If a 0 is encountered, use one flip (decrease `k`).
                k -= 1
            count += 1  # Increase the count for every number included in the window.
        
        maxC = count  # Initialize the maximum count with the initial window size.

        # Second loop to slide the window across the array.
        for i in range(count, len(nums)):
            if nums[i] == 1:
                # If the current number is 1, extend the window.
                count += 1
                maxC = max(maxC, count)  # Update the maximum count if needed.
            else:
                # If the current number is 0, manage the start pointer to adjust the window.
                if nums[start] == 0:
                    # If the number at the start pointer is a flipped 0, move the pointer forward.
                    start += 1
                    continue
                else:
                    # If the number at the start pointer is 1, shrink the window until we
                    # encounter the next 0 in the array.
                    while nums[start] != 0:
                        start += 1
                        count -= 1  # Decrease the count as the window shrinks.
                    # Move past the 0 to complete the window adjustment.
                    start += 1
                    continue
        
        return maxC  # Return the maximum count of consecutive 1s (including flipped 0s).
