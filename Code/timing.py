import time


def time_this_sort(sorter, items_to_sort, display=True):
    '''Prints the time taken for the sorting algorithm to execute.'''
    start = time.time()
    sorter(items_to_sort)
    end = time.time()
    time_taken = f"Sorting time: {(end - start) * 1000} ms."
    # displayed in runner script
    if display is True:
        print(time_taken)
    else:
        return time_taken


def compare_two_sorting_times(sorter1, sorter2):
    '''Speed Test'''

    # 1) Test on Randomly Ordered Input
    print("Random Item Distribution, 100 values")
    # make the dataset
    items = [randint(0, 500) for i in range(100)]
    # time each function
    sort_time1, sort_time2 = (
        time_this_sort(sorter1, items, False),
        time_this_sort(sorter2, items, False)
    )
    # display times
    print(f'First Sorting Algorithm -> {sort_time1}')
    print(f'Second Sorting Algorithm -> {sort_time2} \n')

    # 2) Test on Nearly Sorted Input
    print("Nearly Sorted Distribution, 200 values")
    # make the dataset
    items = list(range(200))
    items.append(5)
    # time each function
    sort_time1, sort_time2 = (
        time_this_sort(sorter1, items, False),
        time_this_sort(sorter2, items, False)
    )
    # display times
    print(f'First Sorting Algorithm -> {sort_time1}')
    print(f'Second Sorting Algorithm -> {sort_time2}\n')

    # 3) Test on Descendingly-Sorted Input
    print("Reverse Sorted Order Distribution, 500 values")
    # make the dataset
    items = list(range(500, 0, -1))
    # time each function
    sort_time1, sort_time2 = (
        time_this_sort(sorter1, items, False),
        time_this_sort(sorter2, items, False)
    )
    # display times
    print(f'First Sorting Algorithm -> {sort_time1}')
    print(f'Second Sorting Algorithm -> {sort_time2}\n')

    # 4) Test on Input with Few Unique
    print("Few Unique Distribution, 700 values")
    # make the dataset
    items = [1] * 200
    items.extend([3] * 300)
    items.extend([2] * 200)
    # time each function
    sort_time1, sort_time2 = (
        time_this_sort(sorter1, items, False),
        time_this_sort(sorter2, items, False)
    )
    # display times
    print(f'First Sorting Algorithm -> {sort_time1}')
    print(f'Second Sorting Algorithm -> {sort_time2}\n')
