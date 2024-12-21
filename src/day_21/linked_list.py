"""
Challenge 141

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to.

Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Running in main():
Fixed_p 2 Move_p 0
Fixed_p 0 Move_p 2
Fixed_p -4 Move_p -4
Linked list [3, 2, 0, -4] has cycle: True
"""

from typing import Optional

class ListNode:
   def __init__(self, x):
      self.val = x
      self.next = None

class LinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
             return False
        
        fixed_p = head
        move_p = head

        while move_p is not None and move_p.next is not None:
            fixed_p = fixed_p.next
            move_p = move_p.next.next
            # print(f"Fixed_p {fixed_p.val} Move_p {move_p.val}")
            if fixed_p == move_p:
                return True
        return False

if __name__ == "__main__":
    array_1 = [3, 2, 0, -4]
    head = []

    # Create a linked list
    for i in range(len(array_1)):
        head.append(ListNode(array_1[i]))
        if i > 0:
            head[i-1].next = head[i]

    # Create a cycle
    head[-1].next = head[1]

    linkedListCycle = LinkedListCycle()
    res = linkedListCycle.hasCycle(head[0])
    print(f"Linked list {array_1} has cycle: {res}")
