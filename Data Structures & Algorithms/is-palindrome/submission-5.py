class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(char for char in s if char.isalnum()).lower()
        l = 0
        for r in range(len(pal)-1, -1, -1):
            if pal[l] != pal[r]:
                return False

            l+=1
            
        return True

    
