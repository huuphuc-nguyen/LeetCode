class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        m, n = len(image), len(image[0])
        old_color = image[sr][sc]

        if old_color == color:
            return image

        def bfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if image[x][y] != old_color:
                return

            image[x][y] = color

            bfs(x-1, y)
            bfs(x+1,y)
            bfs(x,y-1)
            bfs(x,y+1)
        
        bfs(sr,sc)
        return image
        