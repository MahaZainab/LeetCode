class Solution:
    def remove(self, s: str)-> str:
        result=[]
        for char in s:
            if char=="#":
                if result:
                    result.pop()
            else:
                result.append(char)
        return "".join(result)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove(s) == self.remove(t)
        