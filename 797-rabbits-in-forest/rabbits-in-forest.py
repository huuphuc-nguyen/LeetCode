class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0

        # 1 1 2 2 2 2 
        #           x

        # prev = 2
        # fre = 1

        # arr = [
        #     1 2 2
        # ]
        
        prev = -1
        fre = 0
        arr = []

        answers = sorted(answers)

        for ans in answers:
            if ans != prev:
                fre = 1
                arr.append(ans)
                prev = ans
            else: # ans == prev
                fre += 1
                
                if fre <= ans + 1:
                    prev = ans
                else:
                    fre = 1
                    arr.append(ans)
                    prev = ans

        print(arr)
                
        return sum(arr) + len(arr)

    