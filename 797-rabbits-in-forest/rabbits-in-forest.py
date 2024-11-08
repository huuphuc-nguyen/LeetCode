class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0

        prev = -1
        fre = 0
        arr = []

        answers = sorted(answers)

        for ans in answers:
            if ans != prev:
                fre  = 1
                arr.append(ans)
                prev = ans
            else:
                fre += 1
                if fre <= ans + 1:
                    prev = ans
                else:
                    fre = 1
                    arr.append(ans)
                    prev = ans

        return sum(arr) + len(arr)

    