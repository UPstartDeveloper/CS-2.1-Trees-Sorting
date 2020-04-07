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

       Running time: O(p^2) where p is the number of elements in the items
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

       Running time: O(p log(p)), where is the number of items.
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


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
