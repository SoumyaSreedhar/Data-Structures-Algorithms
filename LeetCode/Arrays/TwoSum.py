
class Solution(object):
    def twoSum(self, nums, target):
        mydict = {}
        for index, value in enumerate(nums):
            difference = target-value
            if difference in mydict:
                return [mydict[difference],index]
            mydict[value] = index
           
                
        
