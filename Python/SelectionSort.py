def selection_sort(nums):
    """
    Method that implement selection sort.
    
    Example: 
    random_list_of_nums = [13, 8, 4, 22, 11]
    selection_sort(random_list_of_nums)
    """

    for i in range(len(nums)):
        lowest_value_index = i
        
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
