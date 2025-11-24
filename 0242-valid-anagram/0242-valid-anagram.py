class Solution:
    def hashFunction(self, n):
        return n-97
    def isAnagram(self, s: str, t: str) -> bool:
        arr1=[0]*26
        arr2=[0]*26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            index1=self.hashFunction(ord(s[i]))
            arr1[index1]+=1
            index2=self.hashFunction(ord(t[i]))
            arr2[index2]+=1
        for i in range(26):
            if arr1[i]!=arr2[i]:
                return False
        return True
            
        
        