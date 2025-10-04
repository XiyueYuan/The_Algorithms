### Problem_list
>In this markdown file, the author (Tyy) has recorded his favorite algorithm problems, which are also relatively challenging, and thus worth revisiting and studying repeatedly.

>The Problems are sorted based on the topics

##### Two Pointers
1. *2831: Find the Longest Equal Subarray*
- You are given a 0-indexed integer array nums and an integer k. A subarray is called equal if all of its elements are equal. Note that the empty subarray is an equal subarray. Return the length of the longest possible equal subarray after deleting at most k elements from nums.

Example: 
`Input: nums = [1,3,2,3,1,3], k = 3`
`Output: 3`
Explanation: It's optimal to delete the elements at index `2` and index `4`.
After deleting them, nums becomes equal to `[1, 3, 3, 3]`.
The longest equal subarray starts at `i = 1` and ends at `j = 3` with length equal to `3`. 
It can be proven that no longer equal subarrays can be created.

> Notice the element is not replaced, so the standard `right - left + 1` cannot be applied here. Rather, you can travser the `dict` to see if satisfy the `k` factor.

```python
def longestEqualSubarray(nums: List[int], k: int) -> int:
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)
        res = 0
        for tmp in count.values():
            left = 0
            for right in range(len(tmp)):
                while tmp[right] - tmp[left] + 1 - (right - left + 1) > k:
                    left += 1
                res = max(res, right - left + 1)
        return res
```


