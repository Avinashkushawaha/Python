class Node:
    def __init__(self, data, count):
        self.data = data
        self.count = count
        self.next = None

def array_to_linked_list(arr):
    if not arr:
        return None

    head = None
    current_node = None

    i = 0
    while i < len(arr):
        current_value = arr[i]
        count = 1

        while i + 1 < len(arr) and arr[i + 1] == current_value:
            count += 1
            i += 1

        new_node = Node(current_value, count)

        if not head:
            head = new_node
            current_node = head
        else:

            current_node.next = new_node
            current_node = new_node

        i += 1

        return head                

def print_linked_list(head):
    current = head
    while current:
        print(f"value: {current.data}, count: {current.count}") 
        current = current.next 

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1, 3, 3, 3, 2, 2, 2, 2, 2, 5, 5, 5, 5, 100, 100, 5]

    linked_list_head = array_to_linked_list(arr)

    print_linked_list(linked_list_head)         

