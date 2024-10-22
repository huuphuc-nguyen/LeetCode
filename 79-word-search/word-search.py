class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m, n = len(board), len(board[0])
        
        def dfs(x, y, letter_index):
            if letter_index == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[letter_index]:
                return False
            
            temp = board[x][y]
            board[x][y]="-"

            
            found =  (dfs(x-1,y,letter_index+1) or
                dfs(x+1,y,letter_index+1) or
                dfs(x,y-1,letter_index+1) or
                dfs(x,y+1,letter_index+1))
            
            if found:
                return True
            else:
                board[x][y] = temp
                return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False
        