class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBracket=0
        addRequired=0
        for ch in s:
            if ch =="(":
                openBracket+=1
            else:
                if openBracket>0:
                    openBracket-=1
                else:
                    addRequired+=1
        return openBracket+addRequired
        