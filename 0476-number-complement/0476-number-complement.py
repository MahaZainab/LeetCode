class Solution:
    def findComplement(self, num: int) -> int:
        
        # Get the binary representation length, excluding the '0b' prefix
        binary_length = len(bin(num)) - 2
        
        
        # Create a mask of the same length with all bits set to 1
        # (1 << binary_length) creates a number with 1 followed by binary_length zeros
        # Subtracting 1 from this number gives us binary_length ones
        mask = (1 << binary_length) - 1
        
        # Compute the complement using the mask
        complement = ~num & mask
        
        return complement
#         bitMask=0xFF
#         complement = ~num & bitMask
#         return complement
# #     return ~num
#         binary = bin(num)
#     string = binary[2:]
#     arr = list(string)
#     for i in range(len(arr)):
#         if arr[i] == '0':
#             arr[i] = '1'
#         elif arr[i] == '1':
#             arr[i] = '0'

#     string = "".join(arr)
#     complement = int(string , 2)

#     return complement