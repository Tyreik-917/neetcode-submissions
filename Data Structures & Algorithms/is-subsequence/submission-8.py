class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True

        s_pointer = 0
        t_pointer = 0

        while  t_pointer < len(t):
            print(s_pointer, t_pointer)
            if s[s_pointer] == t[t_pointer]:
                s_pointer+=1
            t_pointer+=1

            if len(s) == s_pointer:
                return True

        return False
                
                


                


                
                    