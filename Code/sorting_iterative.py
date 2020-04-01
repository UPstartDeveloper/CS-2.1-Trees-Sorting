#!python
import sys


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(1, len(items)):
        # the previous item must be less than or equal to its right neighbor
        item = items[i]
        left_neighbor = items[i - 1]
        if left_neighbor > item:
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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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


def find_minimum(items, start, end):
    """Returns the index of smallest value between the start and end indices
       in items.

       Parameters:
       items(list)
       start(int): the index that marks where to start linear search for
                    minimum value
       end(int): the index that indicates where in items we end our search

       Returns: int: the index where the smallest value is found

    """
    minimum = sys.maxsize
    min_index = 0
    for i in range(start, end):
        if items[i] < minimum:
            min_index = i
            minimum = items[i]
    return min_index


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
