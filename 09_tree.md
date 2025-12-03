## Tree

```
Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
```
1. Breadth-first search (BFS)
- Level order
```python
def level_order(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    from collections import deque
    res = []
    q = deque([root]) 
    # initialize deque
    # same as q = deque()
    # q.append(root)
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res
```
1. *Same Tree*
Example 1:
`Input: p = [1,2,3], q = [1,2,3]`
`Output: true`
Example 2:
`Input: p = [1,2], q = [1,null,2]`
`Output: false`
```python 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p) == self.bfs(q)

    def bfs(self, root) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(node)
                q.append(res.left)
                q.append(res.right)
            else:
                res.append(None)
            # notice if node == null, the result should be none
        return res
```
2. *Maximum Depth of Binary Tree*
Example:
`Input: root = [3,9,20,null,null,15,7]`
`Output: 3`
```python
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    from collections import deque
    q, depth = deque([root]), 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return depth 
```
3. *Minimum Depth of Binary Tree*
Example:
`Input: root = [3,9,20,null,null,15,7]`
`Output: 2`
```python
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q, depth = deque([root]), 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if not node.right and not node.left:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
```
4. *Binary Tree Right Side View*
Example: 
`Input: root = [1,2,3,4,null,null,null,5]`
`Output: [1,3,4,5]`
```python
def right_view(root) -> List[int]:
    if not root:
        return []
    q, res = deque([root]), []
    while q:
        last = None
        for _ in range(len(q)):
            node = q.popleft()
            last = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(last)
    return res
```

2. Depth-first search (DFS)
- Preorder
- Inorder
- Postorder
```python
# based on recursion 
def pre_order(root): 
    # left
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)
# based on iteration/stack
def pre_order_stack(root) -> List[int]:
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:  
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
```   
```python
# based on recursion 
def in_order(root):
    # down
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)
# based on iteration/ stack
def in_order_stack(root) -> List[int]:
    res, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
```
```python
# based on recursion 
def post_order(root):
    # right
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)
# based on iteration/ stack
def post_order_stack(root) -> List[int]:
    if not root:
        return []
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]
```
1. *Validate Binary Search Tree*
- Binary Search Tree (BST)
-- The left subtree of a node contains only nodes with keys strictly less than the node's key.
-- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
-- Both the left and right subtrees must also be binary search trees.
Example: 
`Input: root = [5,1,4,null,null,3,6]`
`Output: false`
`# Explanation: The root node's value is 5 but its right child's value is 4.`
```python
# For a Binary Search Tree (BST), an in-order traversal
# always produces a strictly increasing sequence of values
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inorder(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
```
> Optimal
```python
def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float('-inf'), float('inf'))
```
2. *Search in a Binary Search Tree*
```python
# Iteration 
def searchBST(root, target) -> Optional[TreeNode]:
    if not root:
        return None
    while root:
        if root.val == target:
            return root
        elif root.val > target:
            root = root.left
        else:
            root = root.right
    return None
```
```python
# Recursion 
def searchBST(root, target) -> Optional [TreeNode]:
    if not root:
        return None
    elif root.val == target:
        return root
    elif root.val < target:
        return searchBST(root.right, target)
    else:
        return searchBST(root.left, target)
```

---
1. *Symmetric Tree*
Example 1: 
`Input: root = [1,2,2,3,4,4,3]`
`Output: true`
Example 2: 
`Input: root = [1,2,2,null,3,null,3]`
`Output: false`
```python
def symmetric(root) -> bool:
    if not root:
        return True
    q = deque([(root.left, root.right)])
    while q:
        left, right = q.popleft()
        if not left and not right:
            continue
        if not left or not right or left.val != right.val:
            return False
        q.append((left.right, right.left))
        q.append((left.left, right.right))
    return True
```
2. *Path Sum*
`Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1]` 
`targetSum = 22`
`Output: true`
Explanation: The root-to-leaf path with the target sum is shown.

```python
def path_sum(root, target: int) -> bool:
    if not root:
        return False
    def dfs(root, total):
        if not root:
            return False
        total += root.val
        if not root.left and not root.right:
            return total == target
        return dfs(root.left, total) or dfs(root.right, total)
    return dfs(root, 0)
```
3. *Invert Binary Tree*
```python
def invert_tree(root):
    if not root:
        return root
    tmp = root.left
    root.left = invert_tree(root.right)
    root.right = invert_tree(tmp)
    return root
```
4. *Binary Tree Path*
Example: 
`Input: root = [1,2,3,null,5]`
`output: ["1->2->5","1->3"]`
```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root, path):
            if not root:
                return 
            path += str(root.val)
            if not root.left and not root.right:
                ans.append(path)
                return
            path += '->'

            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, '')
        return ans
```
5. *Array to BST*
Time Complexity: O($n^2$)
```python
class Solution:
    def arraytobst(self, nums):
        root = None
        for num in nums:
            root = self.build(root, num)
        return root

    def build(self, root, num):
        if not root:
            return TreeNode(num)
        if num > root.val:
            root.right = self.build(root.right, num)
        elif num <= root.val:
            root.left = self.build(root.left, num)
        return root
```

6. *Sorted Array to BST*
```python
class Solution:
    def sorted_to_bst(self, nums):
        if not nums:
            return None
            
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sorted_to_bst(nums[:mid])
        root.right = self.sorted_to_bst(nums[mid + 1:])

        return root
```

7. *Construct Prefix Trie*

```python
class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.son:
                node.son[c] = Node()
            node = node.son[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.prefix(word)
        return node != None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.prefix(prefix)
        return node != None

    def prefix(self, word: str):
        node = self.root
        for c in word:
            if c not in node.son:
                return None
            node = node.son[c]
        return node
```