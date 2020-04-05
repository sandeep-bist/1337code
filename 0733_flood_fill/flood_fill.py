from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int,
               new_color: int) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    old_color = image[sr][sc]
    if old_color == new_color:
        return image
    fill(image, sr, sc, old_color, new_color)
    return image


def fill(image: List[List[int]], r: int, c: int,
         old_color: int, new_color: int):
    if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
        return
    if image[r][c] == old_color:
        image[r][c] = new_color
        fill(image, r + 1, c, old_color, new_color)
        fill(image, r - 1, c, old_color, new_color)
        fill(image, r, c + 1, old_color, new_color)
        fill(image, r, c - 1, old_color, new_color)
