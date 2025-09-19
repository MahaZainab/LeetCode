class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        output=[]
        for num in nums:
            while output:
                a=output[-1]
                b=num
                g = gcd(a,b)
                if g>1:
                    output.pop()
                    num=(a*b)//g
                else:
                    break
            output.append(num)
        return output

        