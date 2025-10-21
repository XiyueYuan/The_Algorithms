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
---
Matrix Traverse
1. from top left to bottom right
```python
m = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
    [10, 11, 12]
]
res = [1, 4, 2, 7, 5, 3, 10, 8, 6, 11, 9, 12]
```
>notice `(i, j)` in each diagonal remains equal = k
>the number of diagonal in m * n matrix is m + n - 1

```python
class Matrix:
    # from top left to bottom right
    def diagonal_left(self, matrix: List[list]) -> list:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        for k in range(m + n - 1):

            if k <= m - 1:
                i = k
                j = 0
                while 0 <= i < m and 0 <= j < n:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1

            else:
                i = m - 1
                j = k - i
                while i >= 0 and j < n:
                    res.append(matrix[i][j])
                    i -= 1
                    j += 1

        return res

    # from top left to bottom right
    def diagonal_right(self, matrix: List[list]) -> list:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        for k in range(m + n - 1):

            if k < m:
                i = m - 1 - k
                j = 0
                while i < m and j < n:
                    res.append(matrix[i][j])
                    i += 1
                    j += 1

            else:
                i = 0
                j = k - (m - 1) 
                while i < m and j < n:
                    res.append(matrix[i][j])
                    i += 1
                    j += 1

        return res 
```

| Direction | Starting Point `(i, j)` | Movement | Diagonal Relation | Outer Loop |
|------------|--------------------------|-----------|--------------------|-------------|
| ↗ **Bottom-Left → Top-Right** | `(i, j) = (m - 1 - k, 0)` if `k < m`, else `(0, k - (m - 1))` | `i += 1, j += 1` | `i + j = k` | ✅ `for k in range(m + n - 1)` |
| ↘ **Top-Left → Bottom-Right** | `(i, j) = (0, k)` if `k < n`, else `(k - (n - 1), n - 1)` | `i += 1, j -= 1` | `i - j = const` | ✅ same |
| ↙ **Top-Right → Bottom-Left** | `(i, j) = (0, n - 1 - k)` if `k < n`, else `(k - (n - 1), 0)` | `i += 1, j -= 1` | `i + j = const` | ✅ same |
| ↖ **Bottom-Right → Top-Left** | `(i, j) = (m - 1, n - 1 - k)` if `k < n`, else `(m - 1 - (k - (n - 1)), 0)` | `i -= 1, j -= 1` | `i - j = const` | ✅ same |

> Hahahaha.. while debugging relentlessly, a more elegant way is create a `defaultdict` in which stores the element in `key(i + j)` or `key(i - j)`

```python
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9], 
    [10, 11, 12]
]
count = defaultdict(list)
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        count[i - j].append(matrix[i][j])
print(count)

# defaultdict(<class 'list'>, 
# {0: [1, 5, 9], 
# -1: [2, 6], 
# -2: [3], 
# 1: [4, 8, 12], 
# 2: [7, 11], 
# 3: [10]})
```