class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            currentRow = []
            beforeRow = self.getRow(rowIndex - 1)
            for i in range(rowIndex + 1):
                if i == 0 or i == rowIndex:
                    currentRow.append(1)
                else:
                    currentRow.append(beforeRow[i-1] + beforeRow[i])
            return currentRow