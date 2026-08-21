class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        prev = image[sr][sc]
        image[sr][sc] = color
        if sr-1>=0:
            if image[sr-1][sc] == prev:
                self.floodFill(image, sr-1, sc, color)
        if sr+1<len(image):
            if image[sr+1][sc] == prev:
                self.floodFill(image, sr+1, sc, color)
        if sc + 1 < len(image[0]):
            if image[sr][sc+1] == prev:
                self.floodFill(image, sr, sc+1, color)
        if sc - 1 >= 0:
            if image[sr][sc-1] == prev:
                self.floodFill(image, sr, sc-1, color)
        return image