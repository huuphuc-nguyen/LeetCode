class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        chalk_for_one_round = sum(chalk)

        # cfor > given k O(n)
        # cfor == given k O(n)
        # cfor < given k
        k = k%chalk_for_one_round

        # Idea: decrease the k until it is negative => probelm: if k is to gib have to run so many round
        # Solve: calculate the sum of array then use modular
        i = 0

        while True:
            if (i == len(chalk)):
                i = 0
            number_of_needed_chalk = chalk[i]
            k -= number_of_needed_chalk
            if k < 0:
                break
            i += 1

        return i
        
   
        