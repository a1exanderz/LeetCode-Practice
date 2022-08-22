class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        start_pointer, end_pointer = 0, len(s) - 1
        
        while start_pointer < end_pointer:
            
            while not self.isAlphaNum(s[start_pointer]):
                start_pointer += 1
                
                # Edge case of only special characters
                if start_pointer == len(s) - 1:
                    return True

            while not self.isAlphaNum(s[end_pointer]):
                end_pointer -= 1
                
            if s[start_pointer].lower() != s[end_pointer].lower():
                return False
            
            start_pointer += 1
            end_pointer -= 1
            
        return True

    # If need to create your own isalnum function    
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            
        
        
        ### Straightforward solution using built in python string manipulation functions
        
#         # First, convert all uppercase letters into lowercase, remove all spaces and special characters. Runtime O(N), Memory O(N)
#         converted_string = lower(''.join(ch for ch in s if ch.isalnum()))
        
#         # Compare to the palindrome version of the string, Runtime O(N), Memory O(N)
#         return converted_string == converted_string[::-1]
    
        
        ### Attempting a new solution that uses less memory O(1) and does not use built in functions
        ### Compare both ends of the string and return false if something doesn't match
            
        
        