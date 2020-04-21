def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found.

       Runtime Analysis:
       On each iteration or recursive step through this function, half of the
       list elements are eliminated from consideration. On the best case, the
       item is found exactly at the middle index position in the array. This is
       expressed at O(1). On the worst case, the item is not found, or is just
       one index postion off to the left or right of the middle index position.
       Because I use linear search as a helper function in this implementation
       (to handle alphabetization), this case is expressed as O(n*log(n)), or
       more simply O(n) asymptotically. That is to say, although usually binary
       search would be only O(log(n)) complexity, since I am using this
       function to handle both numbers and str values, it is O(n).

       Spacetime Analysis:
       Since this implementation uses linear search, it shares the same
       spacetime complexity as the linear search implementation above: O(n).

    """
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def calculate_middle(low, high):
    '''Return the index of the middle, given lowest and highest indices.'''
    return ((low + high) // 2)


def binary_search_iterative(array, item):
    # init index to start at middle of the array
    low = 0
    high = len(array)
    mid = calculate_middle(low, high)
    # init the list element to start looking at
    elem = array[mid]
    # continually move the mid_index around, until you find the item
    while not elem == item:
        # determine if the element is less than or greater than item
        if elem < item:
            # cut out the lower half of the list,
            low = mid
        else:
            # cut out the upper half of the list
            high = mid
        mid = calculate_middle(low, high)
        # reassign element using new middle, and check again
        elem = array[mid]
        if low == mid and not elem == item:
            return None
    # if the item is found right at the middle
    else:
        return mid
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left, right):
    '''Looks for which index to insert a new array element.'''
    # retrieve the element at the middle index
    mid = calculate_middle(left, right)
    elem = array[mid]
    # check if we have found the element
    if elem == item:
        return mid + 1
    # decide how to move the indices, and try again
    elif elem < item:
        # cut out the lower half of the list
        left = mid
    else:  # elem > item
        # cut out the upper half of the list
        right = mid
    mid = calculate_middle(left, right)
    elem = array[mid]
    # if we are checking indices again, the item's not present
    if left == mid:
        if elem < item:
            return mid + 1
        else:
            return mid
    # call the function with the new subset of the list
    return binary_search_recursive(array, item, left, right)
