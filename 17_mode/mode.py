def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    nums_count = {num: nums.count(num) for num in set(nums)}
    counter = 0
    most_frequent_num = 0
    for (num, count) in nums_count.items():
        if count > counter:
            counter = count
            most_frequent_num = num
    return most_frequent_num