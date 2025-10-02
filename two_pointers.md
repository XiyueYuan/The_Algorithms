## Two Pointers
1. Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.
- A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde" `while `"aec"` is not).

Example 1:
`Input: s = "abc", t = "ahbgdc"`
`Output: true`
Example 2:
`Input: s = "axc", t = "ahbgdc"`
`Output: false`
```python
def isSubsequence(s: str, t: str) -> bool:
    s_pointer = 0
    for t_pointer in range(len(t)):
        if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
            s_pointer += 1
    return s_pointer == len(s)
```
2. You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store. Notice that you may not slant the container.
`Input: height = [1,8,6,2,5,4,8,3,7]`
`Output: 49`
Explanation: The above vertical lines are represented by array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is 49.
```python
def most_water(height: list) -> int:
    left, right = 0, len(height) - 1
    area = 0
    while left < right:
        area = max(area, (right - left) * min(height[right], height[left]))
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
    return area
```
3. You are given an integer array `nums` and an integer `k`. In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array. Return the maximum number of operations you can perform on the array.
`Input: nums = [1,2,3,4], k = 5`
`Output: 2`
Explanation: Starting with `nums = [1,2,3,4]`:
- Remove numbers 1 and 4, then `nums = [2,3]`
- Remove numbers 2 and 3, then `nums = []`
There are no more pairs that sum up to 5, hence a total of 2 operations.
```python
def k_pairs(nums: list, k: int) -> int:
    # nums = [3,1,3,4,3], k = 6
    # -> [1, 3, 3, 3, 4]
    count = 0
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == k:
            count += 1
            left += 1
            right -= 1
        elif total > k:
            right -= 1
        else:
            left += 1
    return count
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) excluding the space used by sorting
```
Another Approach: 
```python
from collections import Counter
def k_pairs(nums: list, k: int) -> int:
    counter = Counter()
    # nums = [3,1,3,4,3], k = 6
    count = 0
    for i, num in enumerate(nums):
        target = k - num
        if counter[target] > 0:
            count += 1
            counter[target] -= 1
        else:
            counter[num] = 1
    return count
#Time Complexity: O(n) because we iterate through the array once with constant-time hash operations. 
# Space Complexity: O(n) because the hash table can store up to n elements in the worst case.
```
4. Longest Substring Without Repeating Characters
- Given a string s, find the length of the longest substring without duplicate characters.
`Input: s = "pwwkew"`
`Output: 3`
Explanation: The answer is `"wke"`, with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```python
def longest_substring(s: str) -> int:
    length = 0
    count = set()
    left = 0
    for i, char in enumerate(s):
        while char in count:
            count.remove(s[left])
            left += 1
        count.add(char)
        length = max(length, i - left + 1)
    return length 
```
5. *Minimize Size Subarray Sum*
- Given an array of __positive integers__ `nums` and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return `0` instead.
`Input: target = 7, nums = [2,3,1,2,4,3]`
`Output: 2`
Explanation: The subarray `[4,3]` has the minimal length under the problem constraint.
```python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    total, ans, left = 0, float('inf'), 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            ans = min(ans, i - left + 1)
            total -= nums[left]
            left += 1
    return ans if ans != float('inf') else 0

# Time Complexity: O(n)
```
6. *Longest Subarray of 1 After Deleting One Element*
`Input: nums = [1,1,0,1]`
`Output: 3`
` # Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.`
```python
def longest_one(nums: List[int]) -> int:
    left, ans = 0, 0
    zero_count = 0
    for right, num in enumerate(nums):
        if num == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        ans = max(ans, right - left)
    return ans
```
7. *Maximum Points You Can Obtain from Cards*
- There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

- In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

- Your score is the sum of the points of the cards you have taken. Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
Example1: 
`cardPoints =[100,40,17,9,73,75]`
`k = 3`
`output = 248`
```python
def maxScore(nums: List[int], k: int) -> int:
    res = total = sum(nums[:k])
    for i in range(1, k+1):
        total = total - nums[k-i] + nums[-i]
        res = max(res, total)

    return res
```