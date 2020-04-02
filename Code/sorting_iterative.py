#!python
tuple = type(())
str = type('')


def compare_tuples(items):
    """Determines which a list of tuples (2D array) is sorted.
       Starts from the beginning of items (assumed that only tuples in items).

    """
    # compare elements in corresponding indices in the items list
    groupings = zip(items)
    # make sure all groupsof data is sorted
    for group in groupings:
        # make sure each group is sorted
        for i in range(1, len(group)):
            left_neighbor = group[i]
            item = group[i - 1]
            # make sure comparing like data types
            if not type(left_neighbor) == type(item):
                return False
            if left_neighbor > item:
                return False
    return True


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.

       Parameters:
       items(list)

       Running time: O(n) in the average case, in which we may require several
                    iterations through the list of items, to find one out of
                    order. The time taken for this step scales in linear
                    proportion to the number of items in items.

        Memory usage: O(1), because in all cases the number of and variety of
                     the variables used in this function does not change.

    """
    for i in range(1, len(items)):
        # the previous item must be less than or equal to its right neighbor
        item = items[i]
        left_neighbor = items[i - 1]
        # if comparing tuples
        if isinstance(left_neighbor, tuple) is True:
            compare_tuples(items)
        # if comparing strings for alphabetization
        if isinstance(left_neighbor, str) is True:
            # Cleaning nonalphabetic characters
            chars = [char for char in left_neighbor if char.isalpha() is True]
            left_neighbor = ''.join(chars)
            chars = [char for char in item if char.isalpha() is True]
            item = ''.join(chars)
            # Insensitizing case
            if left_neighbor.lower() > item.lower():
                return False
        else:
            if left_neighbor > item:
                print(f"Left: {left_neighbor}")
                print(f"Item: {item}")
                return False
    # all items are in ascending sorted order
    return True


def swap_adjacent_items(items, left_index, right_index):
    """Switch elements located in left and right indices in items array.
       When this function is invoked, right element should be less than the
       left element.

    """
    left_item = items[left_index]
    right_item = items[right_index]
    items[left_index] = right_item
    items[right_index] = left_item
    return items


def sort_one_element(items):
    '''Returns True in the edge case where there's only 1 item in items.'''
    if len(items) == 1:
        return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

     Parameters:
     items(list)

     Running time: O(n^2). The runtime complexity of this function scales in
                   proportion to the number of items, on a quadratic scale.
                   This is because we may need to perform n swaps to get each
                   of n elements in its proper position, where n is the number
                   of items. This actually occurs in the worst case scenario,
                   where items is input in perfectly descending order.

     Memory usage: O(1), because this function uses a fixed number of
                   variables.

    """
    sort_one_element(items)
    # everything to the right of this index is assumed to be sorted
    sorted_right = len(items)
    # number of swaps on a given pass
    num_swaps = 0
    while sorted_right > 0:
        # num_swaps = 0
        for i in range(1, sorted_right):
            # num_swaps = 0
            left_index = i - 1
            right_index = i
            # make swaps between adjacent elements as needed
            if items[left_index] > items[right_index]:
                items = swap_adjacent_items(items, left_index, right_index)
                num_swaps += 1
        # slowly move marker for where sorted portion of items being
        sorted_right -= 1


def find_minimum_index(items, start, end):
    """Returns the index of smallest value between the start and end indices
       in items.

       Parameters:
       items(list)
       start(int): the index that marks where to start linear search for
                    minimum value
       end(int): the index that indicates where in items we end our search

       Returns: int: the index where the smallest value is found

    """
    min_index = start
    minimum = items[start]
    for i in range(start, end):
        # if comparing strings, convert to ASCII
        if items[i] < minimum:
            min_index = i
            minimum = items[i]
    return min_index


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
       unsorted item, and repeating until all items are in sorted order.

       Parameters:
       items(list)

       Running time: O(n*(n - i)), where n is the number of items, and i is the
                    number of items we have not sorted already (starting from
                    left).
                    This runtime complexity scales quadratically with respect
                    to the size of n. This is because we need to select the
                    best index to position each of n items. The complexity is
                    not quite O(n^2), because we have the benefit of assuming
                    all elements to the left of our current item (if we
                    started traversing from index 0) are already in perfectly
                    ascending order.

       Memory usage: O(1), because this function uses a fixed number of
                     variables.

    """
    sort_one_element(items)
    # sorted_left is the index to which everything the left of is sorted
    sorted_left = -1
    while sorted_left < len(items) - 1:
        # grab the item at sorted_left index position
        supposed_min = items[sorted_left + 1]
        # search for the minimum among all other items
        other_min_index = find_minimum_index(items, sorted_left + 1,
                                             len(items))
        possible_min = items[other_min_index]
        # if possible_min is less, then it should indeed be swapped
        if possible_min < supposed_min:
            items[sorted_left + 1] = possible_min
            items[other_min_index] = supposed_min
        # move along the sorted portion of items
        sorted_left += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
       order in front of items, and repeating until all items are in order.


       Parameters:
       items(list)

       Running time: O(n*(n - i)), where n is the number of items, and i is the
                    number of items we have sorted already (starting from
                    left).
                    This runtime complexity scales quadratically with respect
                    to the size of n, in the same way as selection sort. One
                    key difference to note is that because we progressively
                    sort items from the right into the left (aka the portion of
                    the array already sorted), this flips the worst case
                    scenario from selection sort. Whereas selection sort
                    performed the worst under a nearly sorted input array, this
                    is the optimal scenario for insertion sort - in terms of
                    this implementation, we see that reflected in the reduction
                    of iterations made in the inner while loop.

       Memory usage: O(1), because this function uses a fixed number of
                     variables.

    """
    # perform as many as n - 1 insertions (n is number of items)
    sort_one_element(items)
    next_index = 1
    while next_index < len(items):
        # figure out the index where the insertion must occur
        insert_at = next_index
        while insert_at >= 1 and items[next_index] <= items[insert_at - 1]:
            insert_at -= 1
        # perform the swap
        insert_item = items.pop(next_index)
        items.insert(insert_at, insert_item)
        # move on to the next index
        next_index += 1
