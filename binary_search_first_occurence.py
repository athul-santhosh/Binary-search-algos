#Binary search fixed point

# naive or brute force approach

A = [-14, -10, -10, 108, 108, 243, 285, 285, 285, 401,903,903]
target = 401
# naive approach

def naive_find(A,target):                           # time O(N). space. O(1)
    for i in range(len(A)):
        if A[i] == target:
            return i
    print("key not in list")


print(naive_find(A,target))

def binary_find(A,target):                          # time O(log n). Space O(1)
    low = 0
    high = len(A)-1

    if A[0] == target:                              # Important Edge case 
        return 0
    
    while low <= high:
        mid = (low + high ) // 2
        #print(mid)
        if target < A[mid]:
            high = mid -1
        elif target > A[mid]:
            low = mid +1
        else:                                       # if edge case is not written then we need to modify the code
            if A[mid -1] != A[mid]:
                return mid
            else:
                high = mid-1


print(binary_find(A,target))







