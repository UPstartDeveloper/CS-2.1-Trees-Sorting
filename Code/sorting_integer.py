#!python
import sys


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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    maximum, minimum = find_max(numbers), find_min(numbers)
    # Create list of counts with a slot for each number in input range
    # using range to reduce the number of indices needed at front of counts
    offset = maximum - minimum
    counts = [0 for _ in range(offset + 1)]
    # Loop over given numbers and increment each number's count
    for number in numbers:
        counts[number - minimum] += 1
    # Loop over counts and overwirtes the input list
    numbers_index = 0
    for number, count in enumerate(counts):
        for j in range(count):
            # use min to write the number, not the count into numbers list
            numbers[numbers_index + j] = number + minimum
        numbers_index += count


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
