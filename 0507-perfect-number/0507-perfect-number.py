class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        sum=1
        for divisor in range(2,int(num**.5)+1):
            if num%divisor==0:
                if divisor==num//divisor:
                    sum+=divisor
                else:
                    sum+=divisor+(num//divisor)
        return num==sum
        