class Solution:
    def findDigitSum(self, num):
        digitSum = 0
        for char in str(num):
            digitSum += int(char)
        return digitSum
    
    def addDigits(self, num: int) -> int:
        num = self.findDigitSum(num)
        while( num // 10 != 0):
            num = self.findDigitSum(num)
        
        return num

