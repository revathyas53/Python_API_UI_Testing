'''Python program to interchange first and last elements in a list


Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]'''


def exchng_fst_lst(A):
    A[0],A[-1]=A[-1],A[0]
    return A


A=[12, 35, 9, 56, 24]

print(exchng_fst_lst(A))

'''Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

'''
def swap_positions(a, p1, p2):
    
    a[p1],a[p2]=a[p2],a[p1]
    
    return a

a = [1, 2, 3, 4, 5]
p1 =2
p2 =5
print(swap_positions(a, p1-1, p2-1))


