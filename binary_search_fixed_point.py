#Binary search fixed point

# naive or brute force approach

nums = [-1,0,1,3,5] 
def linear_fixed_point(nums):              # time O(n) Space O(1)
    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return None


y = linear_fixed_point(nums)
print(y)

def binary_fixed_point(nums):               # time 0(log n) Space O(1)
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high) // 2
        if mid > nums[mid]:                 # we just have to foccus on the right half , 
            low = mid +1                    # left can be ignored so move low to mid +1
        elif mid < nums[mid]:               # vice versa
            high = mid -1
        else:
            return nums[mid]                # if we get a match return 

    return None                             # return None`


z = binary_fixed_point(nums)
print(z)




