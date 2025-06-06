class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverse_list(head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev    
