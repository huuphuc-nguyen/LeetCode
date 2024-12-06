class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        # 1 0 0 0 0
        #         x
        # count = 1

        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i+=1
                continue
            if flowerbed[i] == 0:
                # only 1 spot
                if i == 0 and len(flowerbed) == 1:
                    count +=1 
                    break
                # at the 1st spot:
                if i == 0 and flowerbed[i+1] == 0:
                    count +=1 
                    i+=2
                    continue
                # at the last spot:....1 0 0
                if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    count += 1
                    break
                # at anywhere:
                if i+1 < len(flowerbed) and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                    count +=1 
                    i+=2
                    continue
                i+=1

        return count >= n