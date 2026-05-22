class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []

        for i in range(len(operations)):

            if operations[i] == "+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                sum = num1 + num2
                stack.append(num2)
                stack.append(num1)
                stack.append(sum)

            elif operations[i] == "D":
                score = int(stack[-1]) * 2
                stack.append(score)

            elif operations[i] == "C":
                stack.pop()

            else:
                stack.append(int(operations[i]))
                

        total = 0
        for s in stack:
            total += s

        return total

        