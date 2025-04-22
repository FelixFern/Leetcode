class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative = []
        flatten = []
        zeroExist = False
        sums = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    zeroExist = True
                if matrix[i][j] < 0:
                    negative.append(matrix[i][j])
                    flatten.append(matrix[i][j])
                    sums += -1 * matrix[i][j]
                else:
                    flatten.append(-matrix[i][j])
                    sums += matrix[i][j]

        if (zeroExist):
            negative = []

        if (len(negative) % 2 == 0):
            return sums
        else:
            return sums + 2 * max(flatten)
