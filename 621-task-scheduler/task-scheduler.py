
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        hashmap = {}

        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1
        
        max_frequency = max(hashmap.values())

        blocks = max_frequency - 1

        count_max = 0
        for key in list(hashmap.keys()):
            if hashmap[key] == max_frequency:
                count_max += 1

        total_slot = blocks * (n+1) + count_max

        return max(len(tasks), total_slot)

        