#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    l = len(lst) - 1

    for iteration in range(l):
        for i in range(l - iteration):
            ii = i + 1
            if lst[i] > lst[ii]:
                lst[i], lst[ii] = lst[ii], lst[i]

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    sorted_list = []

    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            sorted_list.append(list2.pop(0))
        elif list2 == []:
            sorted_list.append(list1.pop(0))

        # when comparing 2 lists...
        elif list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))

    return sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    
    # base case
    if len(lst) < 2:
        return lst

    split = int(len(lst) / 2)

    first_half = merge_sort(lst[:split])
    second_half = merge_sort(lst[split:])

    sorted_list = merge_lists(first_half, second_half)

    return sorted_list



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
