class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numStr=""
        for ch in s:
            numStr += str(ord(ch)-ord("a")+1)
        while k>0:
            sum=0
            for ch in numStr:
                sum += int(ch)
            numStr=str(sum)
            k -= 1
        return sum
                