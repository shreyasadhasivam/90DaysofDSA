class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        num = abs(x)
        while num!=0:
            digit = num%10
            rev = rev*10+digit
            num = num//10
        if rev<=-2**31 or rev>=2**31-1:
            return 0
        return -rev if x<0 else rev