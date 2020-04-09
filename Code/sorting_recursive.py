#!python
from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
       and return a new list containing all items in sorted order.

       Running time: O(n + m) where n and m are the amount of elements in
                     items1 and items2, respectively. This is because to merge
                     both lists into one, we need one iteration for per element
                     in both items1 and items2.

       Memory usage: O(n + m) because the size our new list takes up scales
                     linear proportion with the sizes of items1 and items2.

    """
    # make a new list
    merged = list()
    # track idices in both lists of items
    index1, index2 = 0, 0
    # sequence the elements from both items lists
    while index1 < len(items1) and index2 < len(items2):
        # grab items from both items lists to compare
        value1 = items1[index1]
        value2 = items2[index2]
        # decide which is lesser
        if value1 < value2:
            merged.append(value1)
            index1 += 1
        else:
            merged.append(value2)
            index2 += 1
    # if the halves weren't eqaully sized exactly, then add all remaining here
    if index1 < len(items1):
        merged.extend(items1[index1:])
    else:
        merged.extend(items2[index2:])
    # return the new list
    return merged


def split(items):
    '''Splits given list of items into 2 equal halves, and returns them.'''
    mid_index = len(items) // 2
    # return the left and right in a tuple
    return items[:mid_index], items[mid_index:]


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
       sorting each with an iterative sorting algorithm, and merging results
       into a list in sorted order.

       Running time: O(n^2) where n is the number of elements in the items
                     list. The runtime of this function asymptotically scales
                     with the time take by the Insertion Sort algorithm, which
                     is used as a helper twice. Although in the average case
                     Insertion Sort runs in quadratic time, it is important to
                     note that it can also run in only linear time; when a list
                     of only 1 element is passed in, that counts as sorted.

       Memory usage: O(p). The space complexity of this function is dependent
                     upon that of the merge() function, which scales with the
                     size of the input items list.

    """
    # Split items list into approximately equal halves
    left, right = split(items)  # O(p) time
    # Sort each half using any other sorting algorithm
    insertion_sort(left)  # O(p^2 / 2) time
    insertion_sort(right)  # O(p^2 / 2) time
    # Merge sorted halves into one list in sorted order
    return merge(left, right)  # O(n + m) = O(p) time + space


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
       sorting each recursively, and merging results into a list in sorted
       order.

       Running time: O(n log(n)), where n is the number of items.
                     The runtime of this function is asymptotically determined
                     by the number of times an append operation must be
                     performed, in order to merge the elements in sorted order
                     into the array returned by the merge() helper function.
                     We have to perform the append operation for each of p
                     elements, and repeat that step log(p) times, as we merge
                     subsequently larger sub-arrays all back into one.

       Memory usage: O(n), due to the fact we need to depend on the merge()
                     helper function. This means as we sort larger lists, the
                     function requires more memory allocation for the temporary
                     array used in the sorting process.

    """
    # Check if list is so small it's already sorted (base case)
    if len(items) == 1 or len(items) == 0:
        return items  # O(1) time
    else:
        # Split items list into approximately equal halves
        left, right = split(items)  # O(p) time
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        items[:] = merge(sorted_left, sorted_right)  # O(p) time
        return items


def get_pivot(collection):
    """Returns the index of the pivot element in items, after applying the
       'median of three' algorithm.

       How a Pivot is Chosen: "Median of 3"
       1) Take the first item in items (at the zero index)
       2) Take the item from the last index in the array
       3) Take the item at at the middle index in the array
       4) The pivot is the element that is the median of the above three
       5) The three elements go back in the array in sorted order, relative to
          whichever 3 index positions they were pulled from.
          (i.e. if the element pulled from the last index was found to the
           median, it would go back into items at the index the middle element
           orignally occupied).

    """
    # pull out the first, middle, and last elements
    mid, last_index = len(collection) // 2, (len(collection) - 1)
    first, middle, last = (
        collection[0], collection[mid], collection[last_index]
    )
    sub_three = [first, middle, last]
    # sort the three
    insertion_sort(sub_three)
    # place back in the items array
    collection[0] = sub_three[0]
    pivot = collection[mid] = sub_three[1]
    collection[last_index] = sub_three[2]
    # return the index and value of the pivot
    return mid, pivot


def get_left_ref(items, low, high, pivot):
    """Return the index of first element that is less than pivot,
       starting from the left."""
    for i in range(low, high):
        if items_list[i] < pivot:
            return items_list[i], i


def get_right_ref(items, low, high, pivot):
    """Return the index of first element that is greater than pivot,
       starting from the back."""
    for i in range(high, low, -1):
        if items_list[i] < pivot:
            return items_list[i], i


def swap(items, left_index, right_index):
    '''Swaps the index positions of two elements in an array.'''
    items[right_index], items[left_index] = (
        items[left_index], items[right_index]
    )


def partition(items_list, low, high):
    """Return index `p` after in-place partitioning given items in range
       `[low...high]` by choosing a pivot (highest-index element).

       From that range, moving pivot into index `p`, items less than pivot into
       range `[low...p-1]`, and items greater than pivot into range
       `[p+1...high]`.

       Complexity Analysis:
       TODO: Running time: ??? Why and under what conditions?
       TODO: Memory usage: ??? Why and under what conditions?

    """
    # Choose a pivot: highest index element
    pivot = items_list[-1]
    # TODO: Loop through all items in range [low...high]
    left = 0
    right = len(items_list) - 2
    p_index = len(items_list) - 1
    # while left < p_index:
    for i in range(low, high):
        if items_list[left] < pivot:
            left += 1
        if items_list[right] > pivot:
            right -= 1
        # TODO: Move items less than pivot into front of range [low...p-1]
        # TODO: Move items greater than pivot into back of range [p+1...high]
        if items_list[left] > pivot and items_list[right] < pivot:
            swap(items_list, left, right)
    # TODO: Move pivot item into final position [p] and return index p
    swap(items_list, left, p_index)
    return left
    '''
    # Choose a pivot
    p, pivot = get_pivot(items_list)
    # Loop through all items in range [low...high]
    for i in range(low, high):
        # print(i)
        item = items_list[i]
        # Move items less than pivot into front of range [low...p-1]
        if item <= pivot and not i <= p:
            items_list.insert(0,  items_list.pop(i))
            p += 1
        # Move items greater than pivot into back of range [p+1...high]
        elif item > pivot and not i > p:
            items_list.insert(p, items_list.pop(i))
            p -= 1
    # return index p
    # print("Stop iterating")
    return p
    '''
    '''
    p, pivot = get_pivot(items)
    while low < p and high > p:
        low += 1
        high -= 1
        if items[low] > pivot and items[high] <= pivot:
            items[low], items[high] = items[high], items[low]
        if low >= high:
            items[low], pivot = pivot, items[low]
    return p
    '''


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
       around a pivot item and recursively sorting each remaining sublist
       range.

       Complexity Analysis:
       TODO: Best case running time: ??? Why and under what conditions?
       TODO: Worst case running time: ??? Why and under what conditions?
       TODO: Memory usage: ??? Why and under what conditions?

    """
    # TODO: Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) <= 2:
        return items
    # TODO: Partition items in-place around a pivot and get index of pivot
    index_p = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
    if low < high:  # recursive case
        quick_sort(items, low, index_p - 1)
        quick_sort(items, index_p + 1, high)
        return items
    '''
    # TODO: Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) < 2:
        items[:] = items
# print(f'Items: {items}')
        return items
    # TODO: Partition items in-place around a pivot and get index of pivot
    hi_index = len(items)
    p = partition(items, 0, hi_index)
    # after_p = p + 1
    # TODO: Sort each sublist range by recursively calling quick sort
    quick_sort(items[0:p], 0, p - 1)
    quick_sort(items[p:hi_index], p, hi_index)
    '''


'''
# TODO: Check if high and low range bounds have default values (not given)
if low is None and high is None:
    low = 0
    high = len(items)
# TODO: Check if list or range is so small it's already sorted (base case)
if len(items) > 1:
    # TODO: Partition items in-place around a pivot and get index of pivot
    p = partition(items, low, high)
    # TODO: Sort each sublist range by recursively calling quick sort
    hi_index = len(items)
    quick_sort(items[0:p], 0, p - 1)
    quick_sort(items[p:hi_index], p, hi_index)'''
