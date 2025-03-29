odd=[]
nodd=[]
def sortEvenOdd(self, nums):
    for i in range(len(nums)):
        if i%2==0:
            odd.append(nums[i])
        else:
            nodd.append(nums[i])
    odd_sorted=sorted(odd, reverse=True)
    nodd_sorted=sorted(nodd)
    for i in range (len(nums)):
        if i%2==0:
            nums[i]=odd_sorted[i]
        else:
            nums[i]=nodd_sorted[i]
    return(nums)

