class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum=0
        product=1
        while  n>0:
            num=n%10
            Sum+=num
            product*=num
            n //=10
        return product-Sum