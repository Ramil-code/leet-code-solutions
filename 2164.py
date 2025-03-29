odd=[]
nodd=[]
def sortEvenOdd(self, nums):
    for i in range(len(nums)):
        if i%2==0:
            odd.append(nums[i])
        else:
            nodd.append(nums[i])
    nodd_sorted=sorted(odd, reverse=True)
    odd_sorted=sorted(nodd)
    odd_i=0
    nodd_i=0
    for i in range(len(nums)):
        if i%2==0:
            nums[i]=odd_sorted[odd_i]
            odd_i=odd_i+1
        else:
            nums[i]=nodd_sorted[nodd_i]
            odd_i=odd_i+1
    return(nums)

