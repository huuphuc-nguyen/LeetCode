class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        

        # n student
        # n size chalk | sum(chalk) = k, if sum (chalk) < chalk[i]
        # student i use chalk i


        # use k - chalk[i] => if result is negative => return i

        chalk_for_one_round = sum(chalk)

        # cfor > given k O(n)
        # cfor == given k O(n)
        # cfor < given k
        if chalk_for_one_round < k:
            k = k%chalk_for_one_round

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
        
   
        