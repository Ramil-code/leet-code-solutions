def mergeSimilarItems(self, items1, items2):
    total={}
    ret=[]
#Iteration thought the first list
    for value, weight in items1:
        if value in total:
            total[value]+=weight
        else:
            total[value]=weight
#Iteration thought the second list            
    for value, weight in items2:
        if value in total:
            total[value]=+weight
        else:
            total[value]=weight
#sorting the dictionary            
    sorted_total=sorted(total)
#Gatehring the ret list form dictionary
    for value in sorted_keys:
        weight=total[value]
        two=[value,weight]
        ret.append(two)
    return(ret)