from __future__ import annotations 
from typing import List 
from bst import BST 

class BSTEmpty(BST):
    def is_empty(self) -> bool:
        return True 
    
    def is_leaf(self) -> bool:
        return False 
    
    def root(self) -> int:
        """See BST"""
        raise TypeError('root() not supported for empty BST')

    def left(self) -> BST:
        """See BST"""
        raise TypeError('left() not supported for empty BST')

    def right(self) -> BST:
        """See BST"""
        raise TypeError('right() not supported for empty BST')

    def in_order(self) -> list[int]:
        """See BST"""
        return []

    def contains(self, n: int) -> bool:
        """See BST"""
        return False
    
    def num_nodes(self) -> int:
        return 0 
    
    def height(self) -> int:
        return 0

    def min(self) -> int|None:
        """See BST"""
        return None

    def max(self) -> int|None:
        """See BST"""
        return None
    
    def total(self) -> int:
        return 0 

    def mean(self) -> float|None:
        """See BST"""
        return None

    