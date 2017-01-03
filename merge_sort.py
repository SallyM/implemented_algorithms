def merge_sort(input_list):

    # splitting original list in half, then each part in half thru recursion
    # until left and right are each one-element lists
    if len(input_list) > 1:
#         print 'len(input_list)= {}'.format(len(input_list))
        split = len(input_list)//2
        left = input_list[: split]
        right = input_list[split :]
#         print 'split list ', left, right
        # recursion
        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
#         print 'i', i
#         print 'j', j
#         print 'k', k
        while i < len(left) and j < len(right):

            # comparing elements at each position of split lists, then merging them into one list
            if left[i] < right[j]:
                input_list[k] = left[i]
                i += 1
#                 print 'i', i
            else:
                input_list[k] = right[j]
                j += 1
#                 print 'j', j
            k += 1
#             print 'k', k

        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1
#             print 'i', i
#             print 'k', k
#             print 'merged list', input_list
        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
#             print 'j', j
#             print 'k', k
#         print 'merged list', input_list

        return input_list
        
