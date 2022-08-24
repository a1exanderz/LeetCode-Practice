class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # "11" + "1" = 3 + 1 = 4
        # 4 = "100"
        
        # Converting binary to decimal
            # For each digit index in the decimal, add 2^index if digit is 1
        
        # Converting decimal to binary
            # Mod decimal by 2 and save the remainder as the end of the string
            # Divide decimal by 2 and that is the new decimal
            # Do this until decimal is 0
        
        numA = 0
        for index, value in enumerate(a):
            if value == "1":
                numA += 2**(len(a) - 1 - index)
                
        numB = 0
        for index, value in enumerate(b):
            if value == "1":
                numB += 2**(len(b) - 1 - index)
                
        print(numA, numB)
        
        totalSum = numA + numB
        
        if totalSum == 0:
            return "0"
        
        binaryStr = ""
        print("binaryStr", binaryStr, "totalSum", totalSum)
        while totalSum != 0:
            binaryStr = str(totalSum % 2) + binaryStr
            totalSum //= 2
            print("binaryStr", binaryStr, "totalSum", totalSum)
            
        return binaryStr
        
        
        
        
            