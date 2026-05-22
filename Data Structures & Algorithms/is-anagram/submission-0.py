class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        for s_letter in s:
            
            if s_letter in t:
                t = t[:t.find(s_letter)] + t[t.find(s_letter) + 1:]
                continue

            else:
                return False
        
        return True