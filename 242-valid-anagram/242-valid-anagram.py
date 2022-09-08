class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictOne = {}
        dictTwo = {}
        
        for c in s:
            if c in dictOne.keys():
                dictOne[c] += 1
            else:
                dictOne[c] = 1
                
        for c in t:
            if c in dictTwo.keys():
                dictTwo[c] += 1
            else:
                dictTwo[c] = 1
                
        return dictOne == dictTwo