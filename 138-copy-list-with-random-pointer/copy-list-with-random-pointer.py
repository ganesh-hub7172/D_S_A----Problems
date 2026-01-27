class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Create copy nodes and insert them after original nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers to copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copied list
        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            copy_curr.next = curr.next
            curr.next = curr.next.next

            curr = curr.next
            copy_curr = copy_curr.next

        return dummy.next
