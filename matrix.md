#### Matrix
1. __Search a 2D Matrix II__
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.
```python
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
    return False
```
2. __Rotate Matrix__
- rotate n * n clockwisely 90 degree
`Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]`
`Output: [[7,4,1],[8,5,2],[9,6,3]]`
```python
def rotate(matrix) -> void:
    # transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
    for row in matrix:
        row.reverse()
```
