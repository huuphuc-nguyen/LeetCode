class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Create largest range, by creating a left and right pointer
        l, r = 0, len(height) - 1
        maxArea = 0

        # At every part of the range calculate the current area at this width and check against our max area
        while l < r:
            width = r - l
            minHeight = min(height[l], height[r])
            currArea = minHeight * width
            maxArea = max(maxArea, currArea)

            # Reduce the range/width while maintaining the maximum height 
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # Return max area found
        return maxArea
        