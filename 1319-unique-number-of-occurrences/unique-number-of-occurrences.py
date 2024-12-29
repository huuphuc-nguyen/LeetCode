class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = collections.defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        
        # 2 methods: 
        # a. using hash set => space On, time 0n
        # b. using sort and then check adjacent => space 1, time Onlogn

        # choose method a:
        seen = set()
        for num in hashmap.values():
            if num in seen:
                return False
            else:
                seen.add(num)
        
        return True
