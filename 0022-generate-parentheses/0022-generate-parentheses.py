class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtrack(st, openc, close):
            if len(st)==2*n:
                ans.append(st)
                return
            if openc<n:
                backtrack(st+'(', openc+1, close)
            if close<openc:
                backtrack(st+')', openc, close+1)
        
        backtrack("",0,0)
        return ans

        