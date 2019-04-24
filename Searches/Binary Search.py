def binary_search(list,item): # item is the one we are searching for
    low=0
    high=len(list)-1

    while low <=high :
        mid =int((low+high)/2) #list of integers work
        guess=list[mid]
        if guess==item:
            return mid
        if guess > item:
            high=mid-1
        else:
            low=mid+1
    return None  # the item does not exist

# let's check, remember array needs to be sorted for binary search
my_list=[1,3,5,6,8]
print( binary_search(my_list,6))

