### Bit-manipulation
For a number with digits \( d_1, d_2, d_3, \dots, d_n \) in base \( k \):

value = (((d<sub>1</sub>) × k + d<sub>2</sub>) × k + d<sub>3</sub>) × k + ⋯ + d<sub>n</sub>

*for example:*
```python
# print(bin(37)) -> 100101
b = [1, 0, 0, 1, 0, 1]
ans_b = 0
for i in range(len(b)):
    ans_b = ans_b * 2 + b[i]
# ans_b = 37
```