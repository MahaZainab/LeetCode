class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mappair={}
        for c in s:
            if c in mappair:
                mappair[c] += 1
            else:
                mappair[c] = 1
        for c in t:
            if c in mappair:
                mappair[c] -= 1
                if mappair[c]<0:
                    return False
            else:
                False
        for val in mappair.values():
            if val !=0:
                return False
        return True

        # mappair={}
        # for i in range(len(s)):
        #     if s[i] in mappair:
        #         mappair[s[i]] +=1
        #     else:
        #         mappair[s[i]]=1
        # for i in range(len(t)):
        #     if t[i] in mappair:
        #         mappair[t[i]] -=1
        #         if mappair[t[i]]<0:
        #             return False
        #     else:
        #         return False
        # for val in mappair.values():
        #     if val!=0:
        #         return False
        # return True

        # dicts={}
        # dictt={}
        # for i in range(len(s)):
        #     if s[i] in dicts:
        #         dicts[s[i]] +=1
        #     else:
        #         dicts[s[i]]=1

        # for i in range(len(t)):            
        #     if t[i] in dictt:
        #         dictt[t[i]] +=1
        #     else:
        #         dictt[t[i]]=1
        # return dictt==dicts
        