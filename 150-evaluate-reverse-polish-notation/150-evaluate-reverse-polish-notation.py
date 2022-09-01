class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        # 2, 1, +, 3, *
        # 3, 3, *
        # 9
        
        # 4, 13, 5, /, +
        # 4, 2, +
        # 6
        
        # 10, 6, 9, 3, +, -11, *, /, *, 17, +, 5, +
        # 10, 6, 12, -11, *, /, *, 17, +, 5, +
        # 10, 6, -132, /, *, 17, +, 5, +
        # 10, 0, *, 17, +, 5, +
        # 0, 17, +, 5, +
        # 17, 5, +
        # 22
        
#         ## Solution: O((n^2)/2) time and O(n) space
#         # Keep iterating through the array until either * / + - is preceded by two numbers
#         # Then process those 3 values and start from the beginning again
#         # Continue until a value is obtained
        
#         tokenList = ["*", "/", "+", "-"]
        
#         while len(tokens) != 1:
#             for index, token in enumerate(tokens):
#                 if token in tokenList and tokens[index - 1] not in tokenList and tokens[index - 2] not in tokenList:
#                     if token == "*":
#                         tokens[index-2] = int(tokens[index-2]) * int(tokens[index-1])
#                     elif token == "/":
#                         tokens[index-2] = int(int(tokens[index-2]) / int(tokens[index-1]))
#                     elif token == "+":
#                         tokens[index-2] = int(tokens[index-2]) + int(tokens[index-1])
#                     elif token == "-":
#                         tokens[index-2] = int(tokens[index-2]) - int(tokens[index-1])
#                     tokens.pop(index - 1)
#                     tokens.pop(index - 1)
                
#         return tokens[0]


        # 2 1 +
        # 3 3 *
        # 9
        
        # 4 13 5 /
        # 4 2 +
        # 6
        
        # 10 6 9 3 +
        # 10 6 12 -11 *
        # 10 6 -132 /
        # 10 0 *
        # 0 17 +
        # 17 5 +
        # 22

        ## Solution: Try using a stack
        # Add each token to the stack
        # If a * / + - appears, then process the operation and pop all values from the stack. Add new value to stack
        # Proceed until the token list is empty
        
        stack = []
        tokenList = ["*", "/", "+", "-"]
        for token in tokens:
            if token in tokenList:
                v2 = stack.pop()
                v1 = stack.pop()
                if token == "*":
                    stack.append(int(v1) * int(v2))
                elif token == "/":
                    stack.append(int(int(v1) / int(v2)))
                elif token == "+":
                    stack.append(int(v1) + int(v2))
                elif token == "-":
                    stack.append(int(v1) - int(v2))
            else:
                stack.append(token)
            
        return stack[0]
            
                
        
                    
        
        
        