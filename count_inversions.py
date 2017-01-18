# Piggyback on merge_sort algorithm
# Modify merge_sort to count number of elements left in left_half of input_array
# after first right_half element is encountered

def count_inversions(input_array, cnt = 0):

    # splitting original list in half, then each part in half thru recursion
    # until left and right are each one-element lists
    if len(input_array) > 1:
        split = len(input_array)//2
        left = input_array[: split]
        right = input_array[split :]

        # recursion
        cnt += count_inversions(left)
        cnt += count_inversions(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

#             print 'num_inversions beginning of loop', cnt
#            # comparing elements at each position of split lists, then merging them into one list
            if left[i] < right[j]:
                input_array[k] = left[i]
                i += 1
#                 print 'elements', left, right
#                 print 'i', i
            else:
                input_array[k] = right[j]
#                 print 'elements', left, right
#                 print 'inversion', left[i], right[j]
                cnt +=1 + len(left[k+1:])
#                 print input_array[k:]
#                 print input_array[k + 1:]
#                 print 'num_inversions end of loop', cnt
                break
#                 j += 1
#                 print 'j', j
            k += 1
#             print 'k', k

        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1
#             print 'i', i
#             print 'k', k
#             print 'merged list', input_array
        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1
#             print 'j', j
#             print 'k', k
#         print 'merged list', input_array

    return cnt
