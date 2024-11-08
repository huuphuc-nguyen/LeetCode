class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved_map = collections.defaultdict(set)
    
        # Group reserved seats by row
        for row, seat in reservedSeats:
            reserved_map[row].add(seat)
        
        max_groups = 0
        
        # Check each row for available blocks
        for row in reserved_map:
            reserved = reserved_map[row]
            left_block = all(seat not in reserved for seat in [2, 3, 4, 5])
            middle_block = all(seat not in reserved for seat in [4, 5, 6, 7])
            right_block = all(seat not in reserved for seat in [6, 7, 8, 9])
            
            if left_block and right_block:
                max_groups += 2  # Both left and right blocks available
            elif left_block or middle_block or right_block:
                max_groups += 1  # One block available in this row
        
        # Add full rows with no reservations
        max_groups += 2 * (n - len(reserved_map))
        
        return max_groups