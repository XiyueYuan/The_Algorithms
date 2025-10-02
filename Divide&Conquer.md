## Divide & Conquer
1. *Climbing Stairs*
- You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
```python
class Solution: 
    @cache
    def climbingStairs(self, n) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbingStairs(n - 1) + self.climbingStairs(n - 2)
```
2. *Sort an Array*
- Time Complexity: O(nlogn)
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        self.sorting(nums, 0, len(nums) - 1)
        return nums
    
    def sorting(self, nums, left, right):
        if left >= right:
            return 
        mid = left + (right - left) // 2
        self.sorting(nums, left, mid)
        self.sorting(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left: int, mid: int, right: int):
        tmp = []
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        while j <= right:
            tmp.append(nums[j])
            j += 1
        nums[left : right + 1] = tmp
```
3. *Quick Sort*
```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[random.randint(0, len(nums) - 1)]
    left = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + equal + quick_sort(right)
```
