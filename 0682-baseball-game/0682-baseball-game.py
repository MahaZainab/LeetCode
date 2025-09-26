class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr=[]
        for char in operations:
            if char == '+':
                arr.append(arr[-1]+arr[-2])
            elif char== 'C':
                arr.pop()
            elif char == 'D':
                arr.append(arr[-1]*2)
            else:
                arr.append(int(char))
        return sum(arr)

        