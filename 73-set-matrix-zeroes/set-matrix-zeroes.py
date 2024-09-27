class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        row_zero = False  # To check if the first row needs to be zeroed
        col_zero = False  # To check if the first column needs to be zeroed

        # Determine if the first row and first column need to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True

        # Use the first row and first column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the first column
                    matrix[0][j] = 0  # Mark the first row

        # Set the zeros based on marks in the first row and first column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out the first row if needed
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero out the first column if needed
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0
            