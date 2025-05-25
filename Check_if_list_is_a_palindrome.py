def is_list_palindrome(lst):
    
    return lst == lst[::-1] 

print(is_list_palindrome([1, 2, 3, 2, 1])) 

