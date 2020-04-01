def is_sorted(array):
    '''Traverses and makes sure all elements
       are in ascending order.

    '''
    '''Bubble Sort Algorithm
        0. make sure it's not in reverse sorted order 0(n)
        1. iterate over the array (n iterations)
        2. check to make sure successive elements are
           sorted (constant)
           a. if not, then...
               keep moving the inverted (smaller) value
               back to 1 index
        3. move on to the next element

worst case: the array is in reverse sorted order
average: O(n)

(n squared - n) / 2 = 10
[5, 4, 3, 2, 1]
[4, 5, 3, 2, 1]
[4, 3, 5, 2, 1]
[4, 3, 2, 5, 1]
[4, 3, 2, 1, 5]



pass



* Selection Sort *

keep a variable for where the sorted portion of the array
begins (starts at 0, everything to the left of this index
is sorted)

start iterating over the list elements,

like before, we check to make sure adjacent elements are
in ascending order

    if they're not:
        then we move the unsorted marker to where





























    '''
