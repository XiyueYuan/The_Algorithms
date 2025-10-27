1. *Climbing Stairs*
```python
@cache
def stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return stairs(n - 1) + stairs(n - 2)
```
2. *K minimum node in a binary tree*

Example: 
<p align="center">
<img src= 'assets/smbt1.jpg'
width="380"/>
</p>

`Input: root = [2,2,5,null,null,5,7], k = 2`
`Output: 5`
Explanation: The smallest value is 2, the second smallest value is 5.

```python
def findSecondMinimumValue(root: Optional[TreeNode], k: int) -> int:
        res = set()
        def dfs(root):
            if not root:
                return 
            res.add(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = sorted(res)
        return res[k - 1] if len(res) >= k else -1
```