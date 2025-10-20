## Linked List 
```python
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```
1. *Merge Two Sorted List*
- You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = cur = ListNode(0)
        # create sentinel/dummy node
        # compare val and merge the node
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next, list2 = list2, list2.next
                cur = cur.next
            else:
                cur.next, list1 = list1, list1.next
                cur = cur.next
        # connect the left
        cur.next = list1 if list1 else list2
        return dum.next
```
2. *Linked List Cycle*
- Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
```python
# test if the linked list is cycled
def hasCycle(self, head: Optional[ListNode]) -> bool:
    count = set()
    while head:
        if head in count:
            return True
        count.add(head)
        head = head.next
    return False
# notice linked list is hashable 
# memory address is restored in hashmap
```
Another Approach - optimal
```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
3. *Intersections of Two Linked Lists*
Optimal:
```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
# a and b runs both (a + b) distance
# meet in public place c
```
```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    setA = set()
    while headA:
        setA.add(headA)
        headA = headA.next
    while headB:
        if headB in setA:
            return headB
        headB = headB.next
    return None
```
4. *ReverseList*
```python
def reverseList(head: ListNode) -> ListNode:
    cur, prev = head, None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
```
5. *Palindrome Linked List*
`linked_list = [1, 2, 3, 4, 3, 2, 1]`
`return True`

- approach1: 
~reverse the part after the middle 
`-> [1, 2, 3, 1, 2, 3, 4]`
~then 
`head2 = [1, 2, 3, 4]`
~then traverse the two linked lists
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid_node = self.mid(head)
        head2 = self.reverse(mid_node)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

    def mid(self, head) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head) -> ListNode:
        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
```
- approach 2:
~ restore every `val` in a new `list`
~ Space Comlexity: O(n)
```python
def isPalindrome(head: Optional[ListNode]) -> bool:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res == res[::-1]
```
6. *Reorder List*

Example 1:
`Input: head = [1,2,3,4]`
`Output: [1,4,2,3]`

Example 2:
`Input: head = [1,2,3,4,5]`
`Output: [1,5,2,4,3]`

Approach1: 
~find the mid `[3]`
~reverse the part after the middle and break into two 
~`[1, 2], [5, 4, 3]`
~merge two linked lists alternatively
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.mid(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverse(l2)
        self.merge(l1, l2)
            
    def reverse(self, head) -> ListNode:
        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    def mid(self, head) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2) -> ListNode:
        while head1 and head2:
            tmp1 = head1.next
            tmp2 = head2.next
            head1.next = head2
            head1 = tmp1
            head2.next = head1
            head2 = tmp2
```
7. *Add Two Numbers*
- Example1:
`Input: l1 = [2,4,3], l2 = [5,6,4]`
`Output: [7,0,8]`
Explanation: 342 + 465 = 807.

- Example 2:
`Input: l1 = [0], l2 = [0]`
`Output: [0]`

- Example 3:
`Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`
`Output: [8,9,9,9,0,0,0,1]`

```python
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dum = ListNode(0)
    node = dum 
    # create dum for a sentinel node 
    # create node to operate 'next'
    carrier = 0
    # check for carry 
    while l1 or l2 or carrier:
        total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carrier
        node.next = ListNode(total % 10)
        node = node.next
        carrier = total // 10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dum.next

    # Time Complexity: (O(Max(m, n)))
```
