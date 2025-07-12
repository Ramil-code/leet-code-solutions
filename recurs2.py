def SumRecurs (arr):
    if not arr:
        return 0
    else:
        return arr[0]+SumRecurs(arr[1:])

arr=[1,3,5]

print(SumRecurs(arr))