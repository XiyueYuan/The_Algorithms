from __future__ import annotations 
from typing import List 
from abc import ABC, abstractmethod 

class BST(ABC):

    @abstractmethod 
    def is_empty(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def is_leaf(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod 
    def root(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def left(self) -> BST:
        """
        Get the left child of the given tree.

        Returns (BST): the left child

        Raises: TypeError, if called on an empty tree
        """
        raise NotImplementedError

    @abstractmethod
    def right(self) -> BST:
        """
        Get the right child of the given tree.

        Returns (BST): the right child

        Raises: TypeError, if called on an empty tree
        """
        raise NotImplementedError

    @abstractmethod 
    def in_order(self) -> List[int]:
        raise NotImplementedError
    
    @abstractmethod
    def contains(self, n: int) -> bool:
        raise NotImplementedError

    @abstractmethod
    def num_nodes(self) -> int:
        raise NotImplementedError 
    
    @abstractmethod
    def height(self) -> int:
        """
        Get the height of the given tree.

        Returns (int): the height
        """
        raise NotImplementedError
    
    @abstractmethod
    def min(self) -> int|None:
        """the minimum value in the tree"""
        raise NotImplementedError

    @abstractmethod
    def max(self) -> int|None:
        """the maximum value in the tree"""
        raise NotImplementedError
    
    @abstractmethod
    def total(self) -> int:
        raise NotImplementedError


    @abstractmethod
    def mean(self) -> float|None:
        """the average (mean) of all values in the tree"""
        raise NotImplementedError

    