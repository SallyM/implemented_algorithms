# def quick_sort(A):
#     if len(A) == 1:
#         return A
#     else:
#         pivot_idx = partition(A)
#         print pivot_idx
#         l = A[:pivot_idx]
#         r = A[pivot_idx + 1:]
#         quick_sort(l)
#         quick_sort(r)
#     return A
#
# def partition(A):
#     low = randint(0, len(A)-1)
#     high = len(A)
#     pivot = A[low]
# #     print 'pivot beginning of recursive call', pivot
#     left = low
# #     print 'left beginning of recursive call', left
#
#     for i in range(low+1, high):
#         if A[i] < pivot:
#             A[i], A[left] = A[left], A[i]
#             left += 1
# #             print 'left, end of loop', left
#     pivot, A[left] = A[left], pivot
#     return left
def quick_sort(A):
    if len(A) == 1:
        return A
    else:
        low, high = partition(A, 0, len(A))
        print 'sorted'
        print A
        print 'partitioned', low, high

        if low:
            quick_sort(low)
        if high:
            quick_sort(high)
        return A

def partition(A, l, r):
    print l
    print r
    p = A[l]
    print 'pivot = ', p
    i = l + 1
    print 'i before sort = ', i
#     j = l + 1
    if r <= 2:
        if A[r - 1] < p:
            A[l], A[r-1] = A[r-1], A[l]
    for j in range((l + 1), r):
        print 'j = {}; j-th element = {}'.format(j, A[j])
#         print 'right_index before sort = ', j
        if A[j] < p:
#             print 'A[right_index]', A[j], '<', 'pivot', p
            print 'element({}) < pivot({})'.format(A[j], p)
#             print 'A[j]', A[j], ' A[i]', A[i]
#             if j != i:
            A[j], A[i] = A[i], A[j]
#             print 'swapped A[j]', A[j], ' A[i]', A[i]
            print 'sorting'
            print A
            i += 1
            print 'i after sort =', i

        else:
            print 'element({}) > pivot({})'.format(A[j], p)
            print 'this part already sorted'
#             print A
#         print 'j after sort =', j
        print A
#     if j >= i:
    A[l], A[i-1] = A[i-1], A[l]
    print 'swapped pivot and i-th element', A[i-1], A[l]
#     else:
#         A[l], A[-1] = A[-1], A[l]
#         print 'swapped pivot and right-most smaller element', A[-1], A[l]
    return A[:i], A[i:]
#     return A
