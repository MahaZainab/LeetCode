class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount={}
        for char in magazine:
            charCount[char]= charCount.get(char, 0) + 1
        for char in ransomNote:
            if char not in charCount or charCount[char]==0:
                return False
            charCount[char]-=1
        return True