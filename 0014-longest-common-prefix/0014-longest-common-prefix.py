class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for s in strs:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        return prefix

        # if not strs:
        #     return ""
        
        # prefix = strs[0]
        
        # for s in strs[1:]:
        #     # Shrink prefix until it's a prefix of s
        #     while not s.startswith(prefix):
        #         prefix = prefix[:-1]
        #         if not prefix:
        #             return ""
        
        # return prefix
        # # count=0
        # firstword=strs[0]
        # left=0
        # right=1
        # for s in strs:
        #     for ch in s:
        #         similar=0
        #         if firstword[similar]==ch:
        #             count+=1
        #             similar+=1
        #         else:
        #             break;
        #         count=min(count, similar)
        # output=""
        # for i in range(count+1):
        #     output+=firstword[i]
        # return output