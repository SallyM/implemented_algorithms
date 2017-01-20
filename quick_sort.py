def quick_sort(A):
    if len(A) == 1:
        return A
    else:
        pivot_idx = partition(A)
        print pivot_idx
        l = A[:pivot_idx]
        r = A[pivot_idx + 1:]
        quick_sort(l)
        quick_sort(r)
    return A

def partition(A):
    low = randint(0, len(A)-1)
    high = len(A)
    pivot = A[low]
#     print 'pivot beginning of recursive call', pivot
    left = low
#     print 'left beginning of recursive call', left

    for i in range(low+1, high):
        if A[i] < pivot:
            A[i], A[left] = A[left], A[i]
            left += 1
#             print 'left, end of loop', left
    pivot, A[left] = A[left], pivot
#     print 'pivot, end of recursive call', pivot
    return left
