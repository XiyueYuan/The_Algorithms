from __future__ import annotations 
from typing import List 
from bstempty import BSTEmpty
from bst import BST 

class BSTNode(BST):

    _root: int
    _left: BST
    _right: BST
    
    def __init__(self, n: int, left: BST, right: BST):
        """
        Constructor

        Inputs:
            n (int): the root at this node
            left (BST): the left child
            right (BST): the right child
        """
        self._root = n
        self._left = left
        self._right = right 
    
    def is_empty(self) -> bool:
        return False 
    
    def is_leaf(self) -> bool:
        return self._left.is_empty() and self._right.is_empty()
    
    def root(self) -> BST:
        return self._root 
    
    def left(self) -> BST:
        return self._left 
    
    def right(self) -> BST:
        return self._right 

    def in_order(self) -> List[int]:
        return self._left.in_order() + [self._root] + self._right.in_order()
    
    def contains(self, n: int):
        if n > self._root:
            return self._right.contains(n)
        elif n < self._root:
            return self._left.contains(n)
        else:
            return True 
        
    def num_nodes(self) -> int:
        return 1 + self._left.num_nodes() + self._right.num_nodes()
    
    def height(self) -> int:
        return 1 + max(self._left.height(), self._right.height())
    
    def min(self) -> int:
        res = self._left.min()
        return res if res is not None else self._root 
    
    def max(self) -> int:
        res = self._right.max()
        return res if res is not None else self._root

    def total(self) -> int:
        return self._left.total() + self.root + self._right.total() 
    
    def mean(self) -> float:
        return self.total() / self.num_nodes()
    
    

node1 = BSTEmpty()
node2 = BSTNode(10, node1, BSTNode(12, BSTEmpty(), BSTEmpty()))
print(node2.in_order())