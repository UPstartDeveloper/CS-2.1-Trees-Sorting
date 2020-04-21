#!python

from sorting import random_ints
from sorting_iterative import (
    is_sorted,
    bubble_sort,
    selection_sort,
    insertion_sort,
    insertion_sort_using_binary_search,
    cocktail_shaker_sort
)
from sorting_recursive import (
    split_sort_merge,
    merge_sort,
    merge,
    quick_sort,
    get_pivot,
    partition
)
from sorting_integer import counting_sort, bucket_sort
import unittest
import random


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([-3, -1, 3, 5, 7]) is True  # Signed ints in order
        assert is_sorted([-7, -6, 0, 3, 5, 7]) is True  # Zero in order
        assert (is_sorted([1_0000_000, 20_000_000, 30_000_000, 65_454_545_444])
                is True  # Really large ints
                )

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        assert is_sorted([3, 1, 3, -5, -7]) is False  # +/- ints out of order
        assert is_sorted([0, 3, 5, 7, 2]) is False  # Almost in order
        assert is_sorted([2, 3, -3]) is False  # +/- ints out of order
        assert is_sorted([2.0, 3.0, -3.0]) is False  # Ints given as floats

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['A', 'Ba', 'Bba', 'Ccccc']) is True  # changed length
        assert is_sorted(['A', 'b', 'C']) is True  # different case
        # mixig with nonalpanumeric
        assert is_sorted(['A%%', '%b%', '%%C']) is True
        assert is_sorted(['%%', 'B']) is True  # compare with non alpha
        assert is_sorted(['', 'B']) is True  # compare to empty string

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['B', 'Aa', 'Bba', 'Ccccc']) is False  # change length
        assert is_sorted(['B', '%%']) is False  # compare alpha with nonalpha
        # mixing with nonalpanumeric characters and spaces
        assert is_sorted(['x b x ', '%A ', '% G']) is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        # Different lengths
        assert is_sorted([(3, 'A'), (3, 'B', 7)]) is True
        assert is_sorted([(3, 'A', 5, 6), (3, 'B', 7)]) is True

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        # Comparing different data types
        assert is_sorted([('A', 5), (3, 'B')]) is False  # currently failing


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        items4 = [-5, 6, 4, 2, 5]  # negatives and positives
        sort(items4)
        assert items4 == [-5, 2, 4, 5, 6]  # will not work with counting_sort
        items5 = [-5, 2, 0, 5]  # with 0
        sort(items5)
        assert items5 == [-5, 0, 2, 5]  # will not work with counting_sort
        items6 = [5, 6, 7, 1, 2, 4]  # multiple swaps
        sort(items6)
        assert items6 == [1, 2, 4, 5, 6, 7]
        items7 = [3, 2, 1, 0]  # reversed sorted order
        sort(items7)
        assert items7 == [0, 1, 2, 3]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        items5 = [7, 5, 5, 7, 5, 7, 5, 3, 7]
        sort(items5)
        assert items5 == [3, 5, 5, 5, 5, 7, 7, 7, 7]
        items6 = [7, 5, 57, 2, 2, 2, 4]
        sort(items6)
        assert items6 == [2, 2, 2, 4, 5, 7, 57]
        items7 = [-5, 7, -5, 2, 4, -5, -8]
        sort(items7)
        assert items7 == [-8, -5, -5, -5, 2, 4, 7]  # counting_sort fails

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        items4 = ['B', 'D', 'A', '']
        sort(items4)
        assert items4 == ['', 'A', 'B', 'D']
        items5 = ['B', '%', 'A', '']  # decide between different nonalpha chars
        sort(items5)
        assert items5 == ['', '%', 'A', 'B']
        items6 = ['https://', 'hey']  # longer strings
        sort(items6)
        assert items6 == ['hey', 'https://']
        items7 = ['554', '445']  # numerical strings
        sort(items7)
        assert items7 == ['445', '554']

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items

    def test_sort_longer_phrases(self):
        items = 'The Itsy-Bitsy Spider'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items

        items = 'Rat ? A > < Tat Cat ?'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items


class TupleSortTest(unittest.TestCase):
    def test_sorting_small_lists_of_tuples(self):
        # greater comes before first
        items = [(5, 'B'), (3, 'A')]
        sorted_items = sorted(items)
        sort(items)
        assert items == sorted_items
        # switching the placement order data types
        items = [('B', 5), ('A', 3)]
        sorted_items = sorted(items)
        sort(items)
        assert items == sorted_items
        # unevenly sized tuples
        items = [(7, 'A', 5, 6), (3, 'B', 7)]
        sorted_items = sorted(items)
        sort(items)
        assert items == sorted_items


class MergeSortTest(unittest.TestCase):
    '''This suite of tests is specific to the merge function.'''
    def test_merge_on_integers(self):
        '''Two sorted lists are combined in a larger sorted list.'''
        items1 = [1, 2, 4, 5]
        items2 = [3, 6, 7, 8]
        assert merge(items1, items2) == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_merge_on_lists_different_sizes(self):
        '''Two sorted lists are combined in a larger sorted list.'''
        items1 = [1, 2, 4, 5]
        items2 = [3, 8]
        assert merge(items1, items2) == [1, 2, 3, 4, 5, 8]

    def test_merge_on_non_numerical_data(self):
        '''Two sorted lists are combined in a larger sorted list.'''
        # on strings
        items1 = ['A', 'C', 'E', 'X']
        items2 = ['B', 'D', 'Y', 'Z']
        assert merge(items1, items2) == [
            'A', 'B', 'C', 'D', 'E', 'X', 'Y', 'Z'
        ]
        # on tuples
        items1 = [(1, 'A'), (8, 'class')]
        items2 = [(2, 'baboon')]
        assert merge(items1, items2) == [
            (1, 'A'), (2, 'baboon'), (8, 'class')
        ]


class QuickSortTest(unittest.TestCase):
    """
    This suite of tests is specific to the partition and median of three
    helper functions for quick_sort.
    """
    def test_partition(self):
        """
        The elements of an array are split so that the pivot element falls
        into its (ascendingly) sorted position in the final array.
        """
        # one swap at the end
        list = [5, 6, 7, 8, 9, 2]
        partition(list, 0, 5)
        # assert list == [2, 6, 7, 8, 9, 5]  # should be improved in future

    def test_get_pivot_in_correct_range(self):
        """
        The pivot is chosen through a variation of the median of three
        approach.
        This function uses the random.randint function, which complicates the
        process of testing the exact return value. Instead, the test looks to
        check if the return value is in the correct range.
        """
        list = [5, 6, 7, 8, 9, 2]
        assert 0 <= get_pivot(list) <= 5  # between the first and last indices


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = insertion_sort_using_binary_search


if __name__ == '__main__':
    sort = get_sort_function()
    unittest.main()
