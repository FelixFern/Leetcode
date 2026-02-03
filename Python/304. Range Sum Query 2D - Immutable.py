class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n, self.m = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.prefixSum = [[0 for _ in range(self.m)] for _ in range(self.n)]

        self.initPrefixSum()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefixSum[row2][col2]

        topLeft = self.prefixSum[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0  
        topRight = self.prefixSum[row2][col1 - 1] if col1 - 1 >= 0 else 0
        bottomLeft = self.prefixSum[row1 - 1][col2] if row1 - 1 >= 0 else 0
        return self.prefixSum[row2][col2] + topLeft - topRight - bottomLeft

    def initPrefixSum(self):
        for i in range(self.n):
            for j in range(self.m):
                top = self.prefixSum[i - 1][j] if i - 1 >= 0 else 0
                bottom = self.prefixSum[i][j - 1] if j - 1 >= 0 else 0
                diag = self.prefixSum[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0

                self.prefixSum[i][j] = self.matrix[i][j] + top + bottom - diag

                
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)