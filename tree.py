from logging import RootLogger


class TreeNode:

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self) -> list:
        res = []
        def dfs(node):
            if not node:
                return 
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(self)
        return res
            
    def inorder(self) -> list:
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(self)
        return res 
    
    def postorder(self) -> list:
        res = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(self)
        return res 
    
    def findMinMax(self) -> tuple:
        if not self:
            return float('inf'), float('-inf')

        left_min, left_max = self.left.findMinMax() if self.left else (float('inf'), float('-inf'))
        right_min, right_max = self.right.findMinMax() if self.right else (float('inf'), float('-inf'))

        return min(self.val, left_min, right_min), max(self.val, left_max, right_max)
    
    def maxDepth(self) -> int:
        left = self.left.maxDepth() if self.left else 0
        right = self.right.maxDepth() if self.right else 0
        return 1 + max(left, right) 


def buildtree(level: list) -> TreeNode:
    if not level or level[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in level]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            node.left = nodes[li]
        if ri < len(nodes):
            node.right = nodes[ri]
    return nodes[0]

if __name__ == '__main__':
    node = [7, 9, 2, None, 8, 4, 6, None, None, None, None, None, 99, 1, None]
    Tree = buildtree(node)
    print(Tree.preorder())

    