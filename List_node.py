class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
            
        print("None")        