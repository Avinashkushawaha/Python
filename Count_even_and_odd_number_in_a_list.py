def count_even_odd(lst):
    even = len([x for x in lst if x % 2 == 0])
    odd = len(lst) - even 
    return even, odd 

print(count_even_odd([1, 2, 3, 4, 5, 6])) 
