def max_num(arr):
    if len(arr)==1:
        return arr[0]
    else:
        max_list=max_num(arr[1:])
        return arr[0] if arr[0]>max_list else max_list

arr=[1,2,6,8,3]

print(max_num(arr))