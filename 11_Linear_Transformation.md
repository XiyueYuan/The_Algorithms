
1. *1220 Count Vowels Permutation*

- Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

- Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

- Example 1:
    Input: `n = 1`
    Output: `5`
    Explanation: All possible strings are: `"a", "e", "i" , "o" and "u"`.

- Example 2:
    Input: `n = 2`
    Output: `10`
    Explanation: All possible strings are: `"ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua"`.

> Using Matrix to describe the transition of the state
```python
def countVowelPermutation(n: int) -> int:
        import numpy as np 
        if n == 1:
            return 5
        T = np.array([
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0]
            ], dtype = object)
        res = np.linalg.matrix_power(T, n - 1)
        MOD = 10**9 + 7
        return int(np.sum(res) % MOD)
```
2. *N-th Tribonacci Number*

- The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

- Example 1:
    Input: `n = 4`
    Output: 4
    Explanation:
    T_3 = `0 + 1 + 1 = 2`
    T_4 = `1 + 1 + 2 = 4`

> Binary exponentiation + Matrix + Multiply

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        def multiply(A, B) -> list:
            res = [[0] * 3 for _ in range(3)] 
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        res[i][j] += A[i][k] * B[k][j]
            return res

        def matrix_pow(A, p):
            res = [[0] * 3 for _ in range(3)]
            for i in range(3): res[i][i] = 1

            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, A)
                A = multiply(A, A)
                p >>= 1
            return res 

        matrix = [
            [1, 1, 1], 
            [1, 0, 0],
            [0, 1, 0]
        ]
        init = [[1], [1], [0]]
        matrix = matrix_pow(matrix, n - 2)
        res = matrix[0][0] * 1 + matrix[0][1] * 1
        return res
```

3. *1411. Number of Ways to Paint N × 3 Grid*

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

> This is actually a Leetcode Hard question, but if you use matrix to compress the state, only few lines can ace this question
```python
    def numOfWays(self, n: int) -> int:
        # [[3, 2], [2, 2]]
        if n == 1: return 12
        MOD = 10 ** 9 + 7
        aba, abc = 6, 6
        for i in range(n - 1):
            aba, abc = (aba * 3 + abc * 2) % MOD, (aba * 2 + abc * 2) % MOD
        return (aba + abc) % MOD
```

