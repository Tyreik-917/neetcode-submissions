class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome = "".join(char for char in s if char.isalnum()).lower()
        
        l = 0
        for r in range(len(palindrome)-1, -1, -1):
            if palindrome[l] != palindrome[r]:
                return False

            l+=1

        return True