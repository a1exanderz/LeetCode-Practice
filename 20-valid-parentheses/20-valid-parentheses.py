class Solution:
    def isValid(self, s: str) -> bool:
        # Solution: use a stack type data structure: every open bracket is added to the stack, and only a close bracket of the same type as top of stack can remove it. Stack should be empty at end
        
        # Implement a stack using a list and use first in last out method
        
        stack = []
        
        for bracket in s:
            try:
                if bracket == '(' or bracket == '{' or bracket == '[':
                    stack.append(bracket)
                    
                if bracket == ')' and stack[-1] != '(':
                    return False

                if bracket == '}' and stack[-1] != '{':
                    return False

                if bracket == ']' and stack[-1] != '[':
                    return False

                if bracket == ')' and stack[-1] == '(':
                    stack.pop()

                if bracket == '}' and stack[-1] == '{':
                    stack.pop()

                if bracket == ']' and stack[-1] == '[':
                    stack.pop()

            except:
                return False
        
        return not stack