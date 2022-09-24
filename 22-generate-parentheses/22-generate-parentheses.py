class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ()
        # ()(), (())
        # ()()(), (())(), ()(()), (()()), ((()))
        # ()()()(), (())()(), ((()))(), ()((())), ()(())(), ()()(()), (()()()), (()(())), ((())()), (((())))
        
        # Start with several base criteria:
        # Count of open <= n and close <= n
        # Open > close at all times
        # Use recursion to generate all possible outputs, given the criteria above
        
        output = []
        
        def eachCombo(openCount, closeCount, string):
            if openCount == n == closeCount:
                output.append(string)
                return
            
            if openCount < n:
                # print("open", openCount, "close", closeCount, "string", string)
                eachCombo(openCount + 1, closeCount, string + "(")
                    
            if closeCount < openCount:
                # print("open", openCount, "close", closeCount, "string", string)
                eachCombo(openCount, closeCount + 1, string + ")")
                    
        eachCombo(0, 0, "")
                    
        return output
        