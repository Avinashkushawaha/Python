import numpy as np

def count_paths(adj, k):
    mat=np.array(adj)
    res=np.linalg.matrix_power(mat,k)
    return res

adj=[
    [0,1,1],
    [0,0,1],
    [0,0,0]
]
print(count_paths(adj,2))  # [[0 0 1] [0 0 0] [0 0 0]]
