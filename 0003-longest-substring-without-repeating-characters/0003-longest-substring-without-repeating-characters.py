class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s)==0:
            return 0
        if len(s)==1:
            return 1
        left=0
        right=0
        length=0
        diff=0
        unique=set()
        while right<len(s):
            p2ch=s[right]
            if not p2ch in unique:
                unique.add(p2ch)
                right+=1
                diff=right-left
                length=max(length, diff)
            else:
                p1ch=s[left]
                unique.remove(p1ch)
                left+=1
        return length

        