# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(arr, target):

    n = len(arr)

    # find leftIndex
    leftIndex = -1

    # start is the first index of the array
    start = 0

    # end is the last index of the array
    end = n-1

    while(start <= end):
        # mid = (start+end)//2 
        # (start + end) might exceed the range of integers

        # better way to do this
        mid = start + (end - start)//2

        # if target element is equal to the middle element
        if arr[mid] == target:

            # potential answer is found
            leftIndex = mid

            # continue searching in left of mid
            end = mid - 1
        
        # target element is less than middle element
        # search in the left
        elif target < arr[mid]:
            end = mid - 1
        
        # target element is greater than middle element
        # search in the right
        elif target > arr[mid]:
            start = mid + 1


    # find rightIndex
    rightIndex = -1

    # start is the first index of the array
    start = 0

    # end is the last index of the array
    end = n-1

    while(start <= end):
        # mid = (start+end)//2 
        # (start + end) might exceed the range of integers

        # better way to do this
        mid = start + (end - start)//2

        # if target element is equal to the middle element
        if arr[mid] == target:
            # potential answer is found
            rightIndex = mid

            # continue searching in right of mid
            start = mid + 1
        
        # target element is less than middle element
        # search in the left
        elif target < arr[mid]:
            end = mid - 1
        
        # target element is greater than middle element
        # search in the right
        elif target > arr[mid]:
            start = mid + 1

    return [leftIndex,rightIndex]
    

    