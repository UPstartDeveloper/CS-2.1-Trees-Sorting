#!python
import sys
from linkedlist import LinkedList, Node
from sorting_recursive import merge_sort, quick_sort
from sorting_iterative import sort_one_element, insertion_sort
from timing import compare_two_sorting_times
from pprint import pprint
import math


def find_max(numbers):
    '''Linear search for the maximum element in a list of unsorted integers.'''
    maximum = -(sys.maxsize)
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min(numbers):
    '''Linear search for the least element in a list of unsorted integers.'''
    minimum = sys.maxsize
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
       then looping over counts and copying that many numbers into output list.

       Running time: O(n + range), where n is the size of the number list, and
                     range is the difference between the greatest and least
                     values in the distribution of numbers.

                     The runtime of this method scales asymptotically both with
                     respect to the the size of n, and range. For example, in
                     the best case the range of the distribution is not greater
                     than its number of values. In all scenarios we need to
                     spend time making a histogram of the numbers array (O(n)),
                     but when the range is low compared to n, we will not have
                     to spend as much time copying the sorted order of values
                     into numbers. In the worst case scenario, the range is
                     much greater than n - so then we have to combine the
                     linear complexities of both O(n) and O(range), because
                     making the histogram and sorting the original array occur
                     in separate steps.

       Memory usage: O(n + range), because the space required to execute this
                     implementation of counting sort asymptotically scales with
                     linear proportion to the size of the counts array we must
                     construct. The factors that impact how the counts array
                     is populated will depend on how large the numbers array
                     is, as well as how many duplicates it contains (which
                     tends to be inversely proportional to the range).

    """
    # Find range of given numbers (minimum and maximum integer values)
    maximum, minimum = find_max(numbers), find_min(numbers)  # O(2n)
    # Create list of counts with a slot for each number in input range
    # using range to reduce the number of indices needed at front of counts
    offset = maximum - minimum  # O(1)
    counts = [0 for _ in range(offset + 1)]  # O(range + 1)
    # Loop over given numbers and increment each number's count
    for number in numbers:  # O(n)
        counts[number - minimum] += 1
    # Loop over counts and overwrites the input list
    numbers_index = 0
    for number, count in enumerate(counts):  # O(range)
        for j in range(count):  # O(?) - depends on the spread of distribution
            # use min to write the number, not the count into numbers list
            numbers[numbers_index + j] = number + minimum
        numbers_index += count


def make_buckets(numbers):
    '''Use distribution metrics to sort values into buckets.'''
    # compute useful stats about distribution of numbers
    maximum, minimum, number_amt = (
        find_max(numbers),
        find_min(numbers),
        len(numbers)
    )
    if number_amt > 2:
        range_of_num, mean = (maximum - minimum, sum(numbers)/number_amt)
        # calculate interval for each bucket
        interval = range_of_num / number_amt
        # make appropiately sized list of buckets
        num_buckets = number_amt
        buckets = [LinkedList() for _ in range(num_buckets)]
        # using percentile to determine relative location of values
        for number in numbers:
            if number >= 0:
                percentile = number / range_of_num
            else:
                # accounting for negatives by multiplying by -1
                percentile = (number * -1) / range_of_num
            buckets[math.floor(percentile)].append(number)
    else:
        buckets = [LinkedList(numbers)]
    return buckets


def bucket_sort(numbers):
    """Sort given numbers by distributing into buckets representing subranges,
       then sorting each bucket and concatenating all buckets in sorted order.

       Running time: O(n * subranges), where n is the size of the numbers array
       and subranges repesents the size of the duplicates. This is because the
       runtime of this method asymptotically scales with respect to the time
       it takes to place all the elements in buckets. This step will grow with
       the total number of elements being sorted. It will also grow with the
       number of duplicates, because they will end up in the same bucket, and
       that will increase the runtime we use to execute merge sort on that
       bucket. In the best case subranges is much less than n, so the overall
       complexity tends towards O(n). In the worst case all the values are
       duplicates. so they end up in the same bucket, and are sorted in
       the same time it would take to just use merge sort by itself on numbers.

       Memory usage: O(n^2) because the memory required to execute
       this function scales with the size of the buckets array we construct.
       The number of elements in this list is n, and the number of LinkedList
       nodes across all the array positions is also n.

    """
    buckets = make_buckets(numbers)
    # Sort each bucket using any sorting algorithm (recursive or another)
    for index, bucket in enumerate(buckets):  # n iterations
        if bucket.size > 0:  # this has less iterations as duplicates increase
            values = bucket.items()
            merge_sort(values)  # linearithmic time, over only a subset
            buckets[index] = LinkedList(values)  # linear for only a subset
    # Loop over buckets and append each bucket's numbers into output list
    numbers_index = 0
    for index, bucket in enumerate(buckets):  #
        b_size = bucket.size
        if b_size > 0:
            for i in range(b_size):
                numbers[numbers_index + i] = bucket.get_at_index(i)
            numbers_index += b_size


if __name__ == '__main__':
    print('Speed Test: Merge Sort vs. Counting Sort')
    compare_two_sorting_times(merge_sort, counting_sort)

    print('Speed Test: Quick Sort vs. Bucket Sort')
    compare_two_sorting_times(quick_sort, bucket_sort)

    print('Speed Test: Insertion Sort vs. Bucket Sort')
    compare_two_sorting_times(quick_sort, bucket_sort)

    print('Speed Test: Insertion Sort vs. Counting Sort')
    compare_two_sorting_times(quick_sort, counting_sort)
