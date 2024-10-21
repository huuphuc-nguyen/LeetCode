class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = 'x'
                else:
                    queue.append([i, j])

        while queue:
            x,y = queue.popleft()

            # up
            uX = x-1

            if 0 <= uX < m and mat[uX][y] == "x":
                mat[uX][y] = 1 + mat[x][y]
                queue.append([uX,y])

            # down
            dX = x+1

            if 0 <= dX < m and mat[dX][y] == "x":
                mat[dX][y] = 1 + mat[x][y]
                queue.append([dX,y])

            # left
            lY = y-1

            if 0 <= lY < n and mat[x][lY] == "x":
                mat[x][lY] = 1 + mat[x][y]
                queue.append([x,lY])

            # right
            rY = y+1

            if 0 <= rY < n and mat[x][rY] == "x":
                mat[x][rY] = 1 + mat[x][y]
                queue.append([x,rY])

        return mat