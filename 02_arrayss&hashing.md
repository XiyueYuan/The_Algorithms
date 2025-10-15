## Arrays & Hashing
1. *Contains Duplicate*
- Given an integer array `nums`, return `True` if any value appears more than once in the array, otherwise return `False`.
```python
# Sorting
def contains_duplicate(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

# Time Complexity: O(nlogn)
# Space Complexity: O(n) or O(1)
```
```python
# Hashing
def contains_duplicate(nums):
    count = {}
    for key in nums:
        if key in count:
            return True
        else:
            count[key] = 1
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)
```
```python
# Set Length
def contains_duplicate(nums):
    return len(set(nums)) < len(nums)

# Time Complexity: O(n)
# Space Complexity: O(n)
```
2. *isAnagram*
- Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
```python
# Hashing
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_dict, t_dict = {},{}
    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
        t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
    return s_dict == t_dict

# Notice: Using dict.get can avoid exceptions 
# Time Complexity: O(m + n)
# Space Complexity: O(1)
```
```python
# Sorting
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(list(s)) == sorted(list(t))

# Time Complexity: O(nlogn + mlogm)
# Space Complexity: O(1) or O(m + n)
```
```python
# Array & Unicode
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = 26 * [0]
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for var in count:
        if var != 0:
            return False
    return True

# Time Complexity: O(n + m)
# Space Complexity: O(1)
```
3. *Twosum*
- Given an array of integers `nums` and an integer target, return the indices i and j such that `nums[i] + nums[j] == target and i != j`.You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.
    Return the answer with the smaller index first.
```python
# Hashing (One Pass)
def two_sum(nums, target):
    count = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in count:
            return [count[diff], i] if count[diff] < i else [i, count[diff]]
           
        count[num] = i

# Time Complexity: O(n)
# Space Complexity: O(n)
```
```python
# Sorting 
def two_sum(nums, target):
    nindex = []
    for i, num in enumerate(nums):
        nindex.append([num, i])
    nindex.sort()
    i, j = 0, len(nums) - 1
    while i < j:
        cur = nindex[i][0] + nindex[j][0]
        if cur == target:
            return [min(nindex[i][1], nindex[j][1]), 
                    max(nindex[i][1], nindex[j][1])]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []
```
4. *GroupAnagrams*
- Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.
- An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

`Input: strs = ["act","pots","tops","cat","stop","hat"]` 
`Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]`

```python
# Hashing + Sorting
from collections import defaultdict
def group_anagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for char in strs:
        result[''.join(sorted(char))].append(char)
    return list(result.values())

# sort each word and put them in a defaultdict(list)
# defaultdict(list) will return an empty list when asked a non-exist key
# test = ['tca']
# print(sorted(test[0])) -> 'a''c''t'
# print(''.join(sorted(test[0]))) -> act
```
```python
# Hashing + Unicode
from collections import defaultdict
def group_anagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for char in strs:
        count = [0] * 26
        for s in char:
            count[ord(s) - ord('a')] += 1
        result[tuple(count)].append(char)
    return list(result.values())

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
```

---
*collections* package
1. Counter: 
```python
from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter)
# Output: Counter({3: 3, 2: 2, 1: 1})
```
Counter is a sub-class of collections:
`counter.get(key)` to access counts
`counter[key]` to access counts

2. defaultdict
`defaultdict[list]`
`defaultdict[int]`
as mentioned before, return empty `list/float/list...` 

3. `counter.most_common()`
use this method to return a `list`: (element, times)
---
5. *Top K Frequent Elements*
- Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique. You may return the output in any order.

`Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]`

```python
from collections import Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums).most_common(k)
    result = []
    for element, count in counter:
        result.append(element)
    return result

# Time Complexity: O(n log k)
# Space Complexity: O(n)
```
6. *Encode and Decode Strings*
- Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

`Input: ["neet","code","love","you"]`
`Output:["neet","code","love","you"]`
```python
def encode(strs) -> str:
    string = ''
    for char in strs:
        string += str(len(char)) + '#' + char
    return string

def decode(str) -> list:
    result = []
    i = 0
    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        length = int(str[i:j])
        i = j + 1
        j = i + length
        result.append(str[i:j])
        i = j
    return result
```
7. *Products of Array Except Self*
- Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

```Input: nums = [1,2,4,6]```
```Output: [48,24,12,8]```
```python 
def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix = 1
    res = [1] * len(nums)

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]    

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
    return res
```
8. *Merge Strings Alternately*
- You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
`Input: word1 = "abc", word2 = "pqr"`
`Output: "apbqcr"`
`Explanation: The merged string will be merged as so:`
`word1:  a   b   c`
`word2:    p   q   r`
`merged: a p b q c r`
```python 
def mergeAlternately(word1, word2) -> str:
    res = ''
    for i, j in zip_longest(word1, word2, fillvalue = ''):
        res += i + j
    return res
```
*zip*
- return a zip object, an iterator
```python
a = 'hello'
b = 'hhhhhh'
print(list(zip(a, b)))
# [('h', 'h'), ('e', 'h'), ('l', 'h'), ('l', 'h'), ('o', 'h')]
```
9. *Tell if `str a` can be constructed from `str b`*
Example 1: 
`Input: ransomNote = "aa", magazine = "ab"`
`Output: false`
Example 2:
`Input: ransomNote = "aa", magazine = "aab"`
`Output: true`
```python
# put them into a dict then determine if smaller than 0
def construct(a: str, b: str) -> bool:
    cnt = defaultdict(int)
    for c in a:
        cnt[c] += 1
    for c in b:
        cnt[c] -= 1
    return all(c >= 0 for c in cnt.values())
```
 


