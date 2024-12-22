"""
Challenge 21

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Running in main():
Merged linked list:
0
1
1
3
3

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLists:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        current = head

        while l1  and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is not None:
            current.next = l1
        else:
            current.next = l2

        return head

if __name__ == "__main__":
    array1=[0,1,3]
    array2=[1,3]

    l1 = []
    l2 = []

    # Create a linked list
    for i in range(len(array1)):
        l1.append(ListNode(array1[i]))
        if i>0:
            l1[i-1].next = l1[i]

    for i in range(len(array2)):
        l2.append(ListNode(array2[i]))
        if i>0:
            l2[i-1].next = l2[i]

    mergeLists = MergeLists()
    res = mergeLists.mergeTwoLists(l1[0], l2[0])

    print("Merged linked list:")
    while res:
        print(res.val)
        res = res.next

