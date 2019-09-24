def count_sort(A):
    # get max_val in array
    # allocate array from 0 to max_val inclusively
    # in for cycle increment value in index, where index is value in original array
    # 0 <= A[i] <= 9
    max_val = -99999999

    for val in A: # time compl-ty: O(n)
        print(val)
        if max_val < val:
            max_val = val
    
    A_counter = [0 for x in range(0, max_val+1)] # space compl-ty: O(max_val)

    for val in A:
        A_counter[val] += 1 # time_compl-ty: O(max_val)
    
    A_new = []

    for i in range(0, max_val+1): # time compl-ty: O(max_val*n)
        if A_counter[i] > 0:
            while A_counter[i] > 0:
                A_new.append(i)
                A_counter[i] -= 1
    
    return A_new

    # total
    # time compl-ty: O(m*n) + O(m) + O(n) = O(m*n)
    # aux space: O(m)

    # a) wasted space on 0-valued items in A_counter. Need to optimize by using dict
    # b) limit in A value range, can't have negative values, because negative values is 
    #    not aux space (syntactical sugar)
    # c) one more for cycle to get max_val (need to pre-allocate space, statically,
    #    not dynamically)

data = [1, 4, 1, 2, 7, 5, 2, 9]

print(count_sort(data))