class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor=image[sr][sc]
        def helper(x,y):
            if x<0 or x>=len(image):
                return
            if y<0 or y>=len(image[0]):
                return
            if image[x][y]==color:
                return
            if image[x][y] !=startcolor:
                return
            image[x][y]=color
            helper(x-1,y)
            helper(x+1,y)
            helper(x,y+1)
            helper(x,y-1)
        helper(sr,sc)
        return image
        