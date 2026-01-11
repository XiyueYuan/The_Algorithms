### Graph Theory 

1. *Available Captures for Rook*:

You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.
> Using directions to manipulate the chess 

<p align="center">
<img src= 'assets/graph1.Png'
width="350"/>
</p>

Output: 0

<p align="center">
<img src= 'assets/graph2.Png'
width="350"/>
</p>

Output: 3

```python
def numRookCaptures(board: List[List[str]]) -> int:
    rook = (0, 0)
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rook = (i, j)
                break 
    res = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for l, r in directions:
        left, right = rook[0], rook[1]
        
        while True:
            left += l 
            right += r 
            if not (0 <= left <= 7 and 0 <= right <= 7):
                break

            if board[left][right] == 'p':
                res += 1
                break 

            elif board[left][right] == '.':
                continue 

            else:
                break
    return res 
```