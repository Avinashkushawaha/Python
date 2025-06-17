class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

def reverse_linked_list(head):
    prev = None 
    curr = head         