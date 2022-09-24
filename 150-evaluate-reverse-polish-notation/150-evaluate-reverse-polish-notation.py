class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
#         # 2 1 + 3 *
#         # 3 * (1 + 2)
        
#         # 4 13 5 / +
#         # (13 / 5) + 4
        
#         # Every time there are 2 numbers followed by an operation, compute and reorganize
        
#         operations = "/*+-"
#         newTokens = []
        
#         if len(tokens) == 1:
#             output = tokens[0]
#             return output
    
#         for i in range(0, len(tokens)):
#             if tokens[i] in operations and tokens[i-1] not in operations and tokens[i-2] not in operations:
#                 intOne, intTwo = int(tokens[i-2]), int(tokens[i-1])
#                 newTokens.pop()
#                 newTokens.pop()
#                 if tokens[i] == "/":
#                     newTokens.append(str(int(float(intOne) / intTwo)))
#                 elif tokens[i] == "*":
#                     newTokens.append(str(intOne * intTwo))
#                 elif tokens[i] == "+":
#                     newTokens.append(str(intOne + intTwo))
#                 elif tokens[i] == "-":
#                     newTokens.append(str(intOne - intTwo))
#             else:
#                 newTokens.append(tokens[i])
#             # print(newTokens)
        
#         return self.evalRPN(newTokens)

        # Use a stack: every time you get an operation, you compute the two previous numbers
        # O(n) time and O(n) space
        stack = []
        operations = "/*+-"
        for i in range(0, len(tokens)):
            stack.append(tokens[i])
            while stack[-1] in operations:
                one, two = int(stack[-3]), int(stack[-2])
                if stack[-1] == "/":
                    stack.pop()
                    stack.pop()
                    stack[-1] = str(int(float(one) / two))
                elif stack[-1] == "*":
                    stack.pop()
                    stack.pop()
                    stack[-1] = str(one * two)
                elif stack[-1] == "+":
                    stack.pop()
                    stack.pop()
                    stack[-1] = str(one + two)
                elif stack[-1] == "-":
                    stack.pop()
                    stack.pop()
                    stack[-1] = str(one - two)
        
        return stack[0]
            
            
                    