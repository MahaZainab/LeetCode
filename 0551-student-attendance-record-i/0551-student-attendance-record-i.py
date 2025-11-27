class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=0
        for i in range(len(s)):
            if s[i]=='A':
                absent+=1
            if s[i:i+3]=='LLL':
                return False
            if absent >=2:
                return False
        return True
        