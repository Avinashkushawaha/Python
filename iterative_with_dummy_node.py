class Solution:
    def reverseList(self, head):
        dummy = None
        while head:
            temp = head
            head = head.next

            temp.next = dummy
            dummy = temp

        return dummy
        