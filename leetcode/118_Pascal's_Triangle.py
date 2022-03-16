class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            currentRow = []
            lastRow = self.generate(numRows - 1)
            for i in range(numRows):
                if i == 0 or i == numRows - 1:
                    currentRow.append(1)
                else:
                    currentRow.append(lastRow[-1][i-1] + lastRow[-1][i])
            lastRow.append(currentRow)
            return lastRow