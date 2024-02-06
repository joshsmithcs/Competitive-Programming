"""
  Joshua Smith
  1528312

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>
  https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LinkedList.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.
"""
import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def to_string(self):
        curr = self.sentinel.next
        while curr != self.sentinel:
            sys.stdout.write(curr.value)
            curr = curr.next

    def insert_between(self, node, left_node, right_node):
        node.prev = left_node
        node.next = right_node
        left_node.next = node
        right_node.prev = node

cases = int(input())
for i in range(cases):
    inp = input()
    outp = LinkedList()
    cursor = 0
    size = 0
    new_node = None
    for char in inp:
        if char == "<":
            if cursor > 0:
                node = new_node
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                new_node = node.prev
                cursor -= 1
                size -= 1
        elif char == "[":
            cursor = 0
            new_node = outp.sentinel
        elif char == "]":
            cursor = size
            new_node = outp.sentinel.prev
        else:
            curr_node = Node(char)
            if size == 0:
                outp.insert_between(curr_node, outp.sentinel, outp.sentinel)
            elif cursor < size:
                outp.insert_between(curr_node, new_node, new_node.next)
            else:
                outp.insert_between(curr_node, outp.sentinel.prev, outp.sentinel)     
            new_node = curr_node
            size += 1
            cursor += 1      
    outp.to_string()
    print()
        