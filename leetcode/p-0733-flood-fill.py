from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        startColor = image[sr][sc]

        def floodFillRec(
            image: List[List[int]], sr: int, sc: int, newColor: int, startColor: int
        ):
            image[sr][sc] = newColor

            up = sr - 1
            if up > -1:
                upVal = image[up][sc]
                if upVal != newColor and upVal == startColor:
                    floodFillRec(image, up, sc, newColor, startColor)

            left = sc - 1
            if left > -1:
                leftVal = image[sr][left]
                if leftVal != newColor and leftVal == startColor:
                    floodFillRec(image, sr, left, newColor, startColor)

            down = sr + 1
            if down < len(image):
                downVal = image[down][sc]
                if downVal != newColor and downVal == startColor:
                    floodFillRec(image, down, sc, newColor, startColor)

            right = sc + 1
            if right < len(image[sr]):
                rightVal = image[sr][right]
                if rightVal != newColor and rightVal == startColor:
                    floodFillRec(image, sr, right, newColor, startColor)

        floodFillRec(image, sr, sc, newColor, startColor)

        return image
