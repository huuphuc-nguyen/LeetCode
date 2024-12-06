class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        rs=[]
        for amount in candies:
            if amount + extraCandies >= maxCandies:
                rs.append(True)
                continue
            rs.append(False)
        
        return rs

