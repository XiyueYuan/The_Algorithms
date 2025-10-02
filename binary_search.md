## Binary Search
1. *Search a 2D Maxtrix*

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise. You must write a solution in O(log(m * n)) time complexity.
`Input: matrix = [[1,3,5,7],
                  [10,11,16,20],
                  [23,30,34,60]], target = 3`
`Output: true`
```python
# See this 2D Matrix as a x*y length 1D Matrix
# Then do a standard binary search 
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    x, y = len(matrix), len(matrix[0])
    left, right = 0, x * y - 1
    while left <= right:
        mid = (left + right) // 2
        # ex. you get mid = 5, which val = 11 in matrix[1, 1]
        val = matrix[mid // y][mid % y]
        if val == target:
            return True
        elif val > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
    
# Time complexity: O(log(m*n))
```

2. *Find First and Last Position of Element in Sorted Array*
- Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.If target is not found in the array, return `[-1, -1]`.
- You must write an algorithm with O(log n) runtime complexity.
`Input: nums = [5,7,7,8,8,10], target = 8`
`Output: [3,4]`
```python
# O(log n) First Impression -> Binary Search 
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        return [self.Left(nums, target), self.Right(nums, target)]

    def Left(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    def Right(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
```
##### open interval & close interval in Binary Search
```python
# []
def binarysearch(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# ()
def binarysearch(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left
```