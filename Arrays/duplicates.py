from ordered_set import OrderedSet
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = OrderedSet()
        
        for i in range(len(nums)):
            x.append(nums[i])
        
        k = len(x)
        j = 0
        for l in x:
            nums[j] = l
            j+=1
        return k

arr=[-1,0,0,0,0,0,0,3,3,4]
removeDuplicates(arr)
print(arr)