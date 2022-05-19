class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet = set()

        while n != 1:
            strN = str(n)
            tempN = 0
            for i in range(len(strN)):
                tempN += int(strN[i]) ** 2
            n = tempN
            if n in hashSet:
                return False
            else:
                hashSet.add(n)
        return True
