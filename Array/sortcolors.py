
def sortZeroeOneTwo(nums:list[int]) -> list[int]:
    # Brute force Solution
    """
    
    # nums.sort()

    # return nums
    """

    # Better Solution
    """
    cnt0,cnt1,cnt2 = 0,0,0
    for i in range(len(nums)):
        if nums[i] == 0:
            cnt0 +=1
        elif nums[i] == 1:
            cnt1 +=1
        else:
            cnt2 +=1

    for i in range(0,cnt0):
        nums[i] = 0

    for i in range(cnt0,cnt0+cnt1):
        nums[i] = 1
    
    for i in range(cnt0+cnt1,len(nums)):
        nums[i] = 2

    return nums
    """

    #Optimal Solution (Dutch National Flag Algorithm)
if __name__ == "__main__":
    nums = [0, 0, 1, 2, 0, 1]
    Solution = sortZeroeOneTwo(nums)
    print(nums)