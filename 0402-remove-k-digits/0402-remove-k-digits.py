class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while stack and stack[-1]>i and k > 0 :
                stack.pop()
                k -=1
            stack.append(i)
        
        if k > 0:
            stack = stack[:len(stack) - k]
        
        res = "".join(stack)
        # converting stack to string

        res = res.lstrip("0")

        return res if res else "0"
        