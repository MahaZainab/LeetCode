class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=[""]*len(s)
        i=0
        for index in indices:
            result[index]=s[i]
            i+=1
        return "".join(result)