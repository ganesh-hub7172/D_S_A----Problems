class Solution:
    def insertGreatestCommonDivisors(self, head):
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        curr = head
        
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g)
            
            new_node.next = curr.next
            curr.next = new_node
            
            curr = new_node.next
        
        return head
