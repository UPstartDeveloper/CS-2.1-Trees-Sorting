#!python
from sorting_iterative import insertion_sort
from random import randint
from timing import time_this_sort


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
    # track index positions in both lists of items
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
                     by the algorithm and repetitions of the merge function,
                     in order to combine the elements in sorted order.
                     We have to perform the append operation for each of n
                     elements, and repeat that step log(n) times, as we merge
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
       1) Take three random indices in the collection (a Python list)/
       2) The pivot is the element that is the median of the above three
       3) The three elements go back in the array in sorted order, relative to
          whichever 3 index positions they were pulled from.
          (i.e. if the element pulled from the last index was found to the
           median, it would go back into items at the index the middle element
           orignally occupied).

    """
    # pull out three random indices in the collection - will revisit when
    # we can prevent the same index being chosen more than once
    # first_rand = randint(0, len(collection) - 1)
    # second_rand = randint(0, len(collection) - 1)
    # third_rand = randint(0, len(collection) - 1)
    first_index = 0
    mid_index = len(collection) // 2
    last_index = len(collection) - 1
    first, middle, last = (
        collection[first_index],
        collection[len(collection) // 2],
        collection[last_index]
    )
    sub_three = [first, middle, last]
    # sort the three
    insertion_sort(sub_three)
    # print(sub_three)
    # place back in the items array
    collection[first_index] = sub_three[0]
    pivot = collection[mid_index] = sub_three[1]
    collection[last_index] = sub_three[2]
    # print(pivot)
    # print(collection)
    # return the index position pivot
    return first_index


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
            i, pivot = pivot, i
            return items_list[i], i


def swap(items, left_index, right_index):
    '''Swaps the index positions of two elements in an array.'''
    items[right_index], items[left_index] = (
        items[left_index], items[right_index]
    )


def partition(items_list, low, high):
    """Return index `p` after in-place partitioning given items in range
       `[low...high]` by choosing a pivot (lowest-index element).

       From that range, moving pivot into index `p`, items less than pivot into
       range `[low...p-1]`, and items greater than pivot into range
       `[p+1...high]`.

       Complexity Analysis:
       Running time: O(n) where n is the number of items being sorted.
                     This is because the runtime of this function scales in
                     linear proportion with respect to the range of elements
                     between the low and high index positions. In the worst
                     case where we have a list that is sorted in the reverse of
                     our desired order, then we will have to make the maximum
                     of n swaps as we iterate through the items_list.

       Memory usage: O(1) because we partition the items_list in-place.
                     Only a small number of local variables is used for this
                     function, so the space complexity does not change with
                     respect to the size of the input

    """
    '''
    p_index = get_pivot(items_list)
    left_i, right_i = low, high
    pivot = items_list[p_index]
    while left_i < right_i:
        while items_list[left_i] <= pivot and left_i < right_i:
            left_i += 1
        while items_list[right_i] > pivot:
            right_i -= 1
        swap(items_list, left_i, right_i)
    swap(items_list, p_index, left_i)
    return left_i
    '''
    # shoutout to Alex, Ramon, Jerome, Uyen, Alan, and Andrey for your help!
    # choose the lowest index to be the pivot
    p_index = low
    # p_index = get_pivot(items_list)
    # Loop through all items in range [low...high]
    for i in range(low + 1, high + 1):
        # Move items less than pivot into front of range [low...p-1]
        if items_list[i] < items_list[p_index]:
            swap(items_list, i, low)
            i += 1
    # return index p
    return p_index


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
       around a pivot item and recursively sorting each remaining sublist
       range.

       Complexity Analysis:
       Best case running time: O(n log(n))
       Like merge_sort, the quick_sort algorithm sorts n elements by repeating
       a recursive process. It calls on itself log(n) times in cases where the
       pivot chosen partitions the items list in half (aka the median). This
       would make the number of stack frames used grow asymptotically on the
       scale of log(n), because each sub-array leaves us with only half the
       elements as before to sort. Overall, the complexity grows
       linearithmically with respect to the size of the input items list.

       Worst case running time: O(n^2).
       The runtime of the quick sort algorithm hinges upon how close the pivot
       element chosen is to the true median of our dataset. In our
       implementation, in which the first element is chosen as the pivot, that
       makes a reverse sorted list (where the max element becomes our pivot)
       the worst case scenario. This is because quick sort relies upon the
       divide conquer strategy, but in this subproblem only helps us increase
       the amount of sorted elements by 1 element, meaning it scales in O(n)
       time. Because the time to solve each subproblem, aka call the partition
       function is also O(n) (see above), we end up with a quadratic time
       complexity overall.

       Memory usage: O(log n) because the number of recursive calls quick_sort
       pushes onto the call stack scales logarithmically with the size of n.
       This is because in the average case, each subproblem is half the size of
       the one that came before; therefore we can compute the amount of space
       used for all the quick_sort calls total, by repeatedly dividing n by 2.
       Since quick_sort sorts in-place, each of these stack frames uses only
       a constant amount of memory.

    """
    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low = 0
        high = len(items) - 1
    # Recursive case
    if low < high:
        index_p = partition(items, low, high)
        quick_sort(items, low, index_p - 1)
        quick_sort(items, index_p + 1, high)


if __name__ == '__main__':
    items = [3, 1, 5, 6, 2]
    quick_sort(items)
    print(items)
    '''# Speed Test: Merge Sort vs. Quick Sort

    # 1) Test on Randomly Ordered Input
    print("Random Item Distribution, 100 values")
    # make the dataset
    items = [randint(0, 500) for i in range(100)]
    # time each function
    m_sort_time, q_sort_time = (
        time_this_sort(merge_sort, items, False),
        time_this_sort(quick_sort, items, False)
    )
    # display times
    print(f'Merge Sort -> {m_sort_time}')
    print(f'Quick Sort -> {q_sort_time} \n')

    # 2) Test on Nearly Sorted Input
    print("Nearly Sorted Distribution, 200 values")
    # make the dataset
    items = list(range(200))
    items.append(5)
    # time each function
    m_sort_time, q_sort_time = (
        time_this_sort(merge_sort, items, False),
        time_this_sort(quick_sort, items, False)
    )
    # display times
    print(f'Merge Sort -> {m_sort_time}')
    print(f'Quick Sort -> {q_sort_time}\n')

    # 3) Test on Descendingly-Sorted Input
    print("Reverse Sorted Order Distribution, 500 values")
    # make the dataset
    items = list(range(500, 0, -1))
    # time each function
    m_sort_time, q_sort_time = (
        time_this_sort(merge_sort, items, False),
        time_this_sort(quick_sort, items, False)
    )
    # display times
    print(f'Merge Sort -> {m_sort_time}')
    print(f'Quick Sort -> {q_sort_time}\n')

    # 4) Test on Input with Few Unique
    print("Few Unique Distribution, 700 values")
    # make the dataset
    items = [1] * 200
    items.extend([3] * 300)
    items.extend([2] * 200)
    # time each function
    m_sort_time, q_sort_time = (
        time_this_sort(merge_sort, items, False),
        time_this_sort(quick_sort, items, False)
    )
    # display times
    print(f'Merge Sort -> {m_sort_time}')
    print(f'Quick Sort -> {q_sort_time}\n')

    print('And the Winner is: Merge Sort!!')'''
