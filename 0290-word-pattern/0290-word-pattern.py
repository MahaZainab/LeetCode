class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # handles multiple spaces cleanly
        if len(pattern) != len(words):
            return False

        patternmap = {}   # maps word -> char
        used = set()      # chars already mapped to some word

        left = 0
        for ch in pattern:
            w = words[left]
            if w in patternmap:
                if patternmap[w] != ch:      # word already mapped to a different char
                    return False
            else:
                if ch in used:               # another word already uses this char
                    return False
                patternmap[w] = ch
                used.add(ch)
            left += 1

        return True
