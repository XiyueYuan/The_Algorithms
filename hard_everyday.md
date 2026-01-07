### A hard question a day, just for fun
42. Trapping Rain Water
```python
def trap(height: List[int]) -> int:
    stack = []
    res = 0
    for i, num in enumerate(height):
        while stack and height[stack[-1]] < num:
            mid = stack.pop()
            if not stack:
                break 
            right, left = i, stack[-1]
            water_height = min(height[left], height[right]) - height[mid]
            width = right - left - 1
            res += water_height * width
        stack.append(i)
    return res
```
2321. Maximum Score Of Spliced Array
```python
def maximumsSplicedArray(nums1: List[int], nums2: List[int]) -> int:
    # diff = num1 - num2
    # num1_max = num2 + diff(max)
    # num2_max = num1 - diff(min)

    diff = [0] * len(nums1)
    for i in range(len(nums1)):
        diff[i] = nums1[i] - nums2[i]

    tmp1 = tmp2 = smax = smin = diff[0]
    for i in range(1, len(diff)):
        tmp1 = max(tmp1 + diff[i], diff[i])
        smax = max(tmp1, smax)

        tmp2 = min(tmp2 + diff[i], diff[i])
        smin = min(tmp2, smin)
    return max(
        sum(nums1), 
        sum(nums2), 
        sum(nums2) + smax,
        sum(nums1) - smin
    )
```
1289. Minimum Falling Path Sum II
> Non-zero shifts = track two minimums 
```python
def minFallingPathSum(self, grid: List[List[int]]) -> int:
    n = len(grid)
    if n == 1:
        return grid[0][0]
    dp = [grid[0]] + [[0] * n for _ in range(n - 1)]
    for i in range(1, n):
        min1, min2 = 100, 100
        tmp = sorted(dp[i - 1])
        min1, min2 = tmp[0], tmp[1]
        for j in range(n):
            if dp[i - 1][j] != min1:
                dp[i][j] = grid[i][j] + min1
            else:
                dp[i][j] = grid[i][j] + min2 
    return min(dp[-1])
```
> sentinel increases robutness
84. Largest Rectangle in Histogram
```python
def largestRectangleArea(heights: List[int]) -> int:
    heights = [0] + heights + [0]
    stack = []
    res = 0
    for i, num in enumerate(heights):
        while stack and heights[stack[-1]] > num:
            tmp = stack.pop()
            height = heights[tmp]
            width = i - stack[-1] - 1
            res = max(res, height * width)
        stack.append(i)
    return res
```
239. Sliding Window Maximum
```python
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []
    for i, num in enumerate(nums):
        while q and nums[q[-1]] <= num:
            q.pop() 
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```
135. Candy
316. Remove Duplicate Letters
410. Split Array Largest Sum
456. 132 Pattern
321. Create Maximum Number
2398. Maximum Number of Robots Within Budget
1696. Jump Game VI
198. House Robber II
309. Best Time to Buy and Sell Stock with Cooldown
123. Best Time to Buy and Sell Stock III
188. Best Time to Buy and Sell Stock IV
221. Maximal Square
279. Perfect Squares
494. Target Sum
91. Decode Ways
801. Minimum Swaps To Make Sequences Increasing
1411. Number of Ways to Paint N × 3 Grid
312. Burst Balloons
546. Remove Boxes
1000. Minimum Cost to Merge Stones
375. Guess Number Higher or Lower II
664. Strange Printer
877. Stone Game
486. Predict the Winner
1140. Stone Game II
1690. Stone Game VII
1039. Minimum Score Triangulation of Polygon
207. Course Schedule
210. Course Schedule II
269. Alien Dictionary
743. Network Delay Time
787. Cheapest Flights Within K Stops
847. Shortest Path Visiting All Nodes
815. Bus Routes
1192. Critical Connections in a Network
332. Reconstruct Itinerary
864. Shortest Path to Get All Keys
124. Binary Tree Maximum Path Sum
968. Binary Tree Cameras
1372. Longest ZigZag Path in a Binary Tree
834. Sum of Distances in Tree
968. Binary Tree Cameras
865. Smallest Subtree with all the Deepest Nodes
1028. Recover a Tree From Preorder Traversal
1339. Maximum Product of Splitted Binary Tree
979. Distribute Coins in Binary Tree
543. Diameter of Binary Tree
460. LFU Cache
432. All O(1) Data Structure
295. Find Median from Data Stream
715. Range Module
850. Rectangle Area II
828. Count Unique Characters of All Substrings
940. Distinct Subsequences II
899. Orderly Queue
975. Odd Even Jump
1937. Maximum Number of Points with Cost