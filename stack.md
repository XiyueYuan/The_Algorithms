## Stack
1. Valid Parentheses
You are given a string s consisting of the following characters: `'(', ')', '{', '}', '[' and ']'`. The input string s is valid if and only if: Every open bracket is closed by the same type of close bracket. Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. Return `true` if s is a valid string, and `false otherwise.

`Input: s = "[(])"`
`Output: false`
```python
def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop(-1)
    return not stack 
# LIFO: last in first out 
# push & pop 
# left: push into stack
# right: if stack and stack[-1] == mapping[char], pop stack[-1]
```
2. Reverse Polish Notation 
*__list to operation__*
`Input: tokens = ["1","2","+","3","*","4","-"]`
`Output: 5`
`Explanation: ((1 + 2) * 3) - 4 = 5`
*__operation to list__*
`((1 + 2) * 3) - 4`
`Output: tokens = ["1","2","+","3","*","4","-"]`
```python
class Convert:
    def apply(self, op: str, num1, num2):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        else:
            return int(num1 / num2)
            
    def list_to_operation(self, tokens) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(self.apply(
                    token, num2, num1
                ))
        return stack.pop()

    def operation_to_list(self, operation: str) -> list:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        ops = []
        tokens = operation.split()
        for token in tokens:
            if token.isdigit():  
                output.append(token)
            elif token in precedence: 
                while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[token]:
                    output.append(ops.pop())
                ops.append(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    output.append(ops.pop())
                ops.pop() 
        while ops:
            output.append(ops.pop())
        return output
```
3. Minstack
Design a stack class that supports the push, pop, top, and getMin operations.
`MinStack()` initializes the stack object.
`void push(int val)` pushes the element val onto the stack.
`void pop()` removes the element on the top of the stack.
`int top()` gets the top element of the stack.
`int getMin()` retrieves the minimum element in the stack.
Each function should run in O(1)time.
```python
class Minstack:
    def __init__(self):
        self.stack = []
        self.stack_min = []
    
    def push(self, var:int) -> None:
        self.stack.append(var)
        if not self.stack_min or var <= self.stack_min[-1]:
            self.stack_min.append(var)
    
    def pop(self) -> None:
        top = self.stack.pop()
        if self.stack_min[-1] == top:
            self.stack_min.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def get_min(self) -> int:
        return self.stack_min[-1]
        
    #O(1) Time Complexity to get_min
```
4. *Decode String*
- Example 1:
`Input: s = "3[a]2[bc]"`
`Output: "aaabcbc"`
- Example 2:
`Input: s = "3[a2[c]]"`
`Output: "accaccacc"`
```python
def decodeString(s: str) -> str:
    stack = []
    for i, c in enumerate(s):
        if c != ']':
            stack.append(c)
        else:
            st = ''
            while stack[-1] != '[':
                # ['4', '5'] -> '45'
                st = stack.pop() + st
            # pop '['
            stack.pop()
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * st)
    return ''.join(stack)
```

