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
