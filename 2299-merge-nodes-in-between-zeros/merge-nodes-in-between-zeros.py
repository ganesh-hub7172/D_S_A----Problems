class Solution:
    def mergeNodes(self, head):
        dummy = ListNode(0)
        tail = dummy
        current_sum = 0
        node = head.next  # skip the first 0

        while node:
            if node.val == 0:
                # End of current segment
                if current_sum != 0:
                    tail.next = ListNode(current_sum)
                    tail = tail.next
                    current_sum = 0
            else:
                current_sum += node.val
            node = node.next

        return dummy.next
