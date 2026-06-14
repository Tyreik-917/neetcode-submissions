class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        stack = []

        for word in s:
            if word in bracket:
                if stack and stack[-1] == bracket[word]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(word)


        return True if not stack else False

