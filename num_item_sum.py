def num_sum(arr):
    if not arr:
        return 0
    else:
        return 1 + num_sum(arr[1:])
    
arr=[1,3,5,6]
print(num_sum(arr))