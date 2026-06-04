class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hashmap = {}
        t_hashmap = {}

        for s_letter in s:
            if s_letter in s_hashmap:
                s_hashmap[s_letter]+=1

            else:
                s_hashmap[s_letter] = 1

        for t_letter in t:
            if t_letter in t_hashmap:
                t_hashmap[t_letter]+=1

            else:
                t_hashmap[t_letter] = 1

        return s_hashmap == t_hashmap