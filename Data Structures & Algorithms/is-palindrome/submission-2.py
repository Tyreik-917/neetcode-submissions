class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome = "".join([word for word in s if word.isalnum()]).lower()
       
        l, r = 0, len(palindrome) - 1

        while l < r:
            if palindrome[l] != palindrome[r]:
                return False

            else:
                l+=1
                r-=1

        return True