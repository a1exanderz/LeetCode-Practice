class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use a two pointer method
        # Start from both ends of the string. If the characters are not equal, return false
        
        # If the indexes are the same, then the character must be the same
        # If the indexes cross, end
        
        fwd = 0
        rev = len(s) - 1
        
        while fwd < rev:
            while not self.alphanum(s[fwd]) and fwd < rev:
                fwd += 1
            while not self.alphanum(s[rev]) and fwd < rev:
                rev -= 1
            if s[fwd].lower() != s[rev].lower():
                return False
            
            # print(fwd, s[fwd].lower(), rev, s[rev].lower())
            
            fwd += 1
            rev -= 1
            
        return True
    
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )
            
    
    
   