### Bit-manipulation
For a number with digits $(d_1, d_2, \dots, d_n)$ in base $k$:

$$
\text{value} = (((d_1) \times k + d_2) \times k + d_3) \times k + \dots + d_n
$$

*for example:*
```python
# print(bin(37)) -> 100101
b = [1, 0, 0, 1, 0, 1]
ans_b = 0
for i in range(len(b)):
    ans_b = ans_b * 2 + b[i]
# ans_b = 37
```
