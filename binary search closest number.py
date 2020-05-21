nums = [1,3,5,6,7,8,9,12,13,17,19,21,25,28,29,78]    

# finding the closest number to the target
# naive or brute force appoach

def bruteclosesest(nums,target):                        # time O(n) space O(n)
    result = []
    for i in range(len(nums)):
        result.append(abs(nums[i] - target))
    return nums[result.index(min(result))]             # logic
#print(bruteclosesest(nums,97))

 
def binary_closeset(nums,target):                       # time O(log n)    space O(1)
    low = 0
    high = len(nums) - 1

    min_diff = float("inf")                             # setting to a large value close to infinity
    closes_num = None
    
    # edge cases 
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]

    # binary search 

    while low <= high:
        #we calculate mid

        mid = (low + high ) // 2 
        print(mid,nums[mid])

        #we find the min_diff_left and min_diff_right
        if mid +1 < len(nums):                                             # important check
            min_diff_right = abs(nums[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(nums[mid-1] - target)

        #  updating the min_diff and closest num

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closes_num = nums[mid + 1]
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closes_num = nums[mid - 1]

        #binary search algo

        if target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid -1
        else:
            return nums[mid]

    return closes_num

y = binary_closeset(nums,89)
print(y)
print(len(nums))


        






