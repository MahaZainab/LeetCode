class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        MapforPara={")": "(", "}": "{", "]": "["}
        for c in s:
            if c in MapforPara:
                if stack and stack[-1]==MapforPara[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
        