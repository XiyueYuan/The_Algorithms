### Stack
##### Monotonic Stack
1. *Maximum Width Ramp*

Example: 
`Input: nums = [6,0,8,2,1,5]`
`Output: 4`
Explanation: The maximum width ramp is achieved at `(i, j) = (1, 5)`: `nums[1] = 0` and `nums[5] = 5`.
Example 2:

`Input: nums = [9,8,1,0,1,9,4,0,4,1]`
`Output: 7`
Explanation: The maximum width ramp is achieved at `(i, j) = (2, 9): nums[2] = 1 and nums[9] = 1`.

```python
def maxWidthRamp(nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        ans = 0
        for j in range(len(nums) - 1, - 1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack[-1])
                stack.pop()
        return ans
```

2. *402 Remove k nums*
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
- Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

```python
def removeKdigits(num: str, k: int) -> str: 
    stack = []
    for c in num:
        while stack and k > 0 and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    while k > 0:
        stack.pop()
    res = ''.join(stack).lstrip('0')
    return res if res else '0
```
