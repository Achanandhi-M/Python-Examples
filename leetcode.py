#https://leetcode.com/problems/roman-to-integer/    

#change this code in simple

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
        return num

# Instantiate the Solution class
solution = Solution()

# Provide the Roman numeral input
input_roman = "IV"

# Call the romanToInt method and get the result
result = solution.romanToInt(input_roman)

# Print the result
print(result)



