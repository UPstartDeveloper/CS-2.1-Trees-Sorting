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
