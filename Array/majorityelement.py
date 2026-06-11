def majorityelement(nums):
    # Brute Force
    """
    cnt = 0
    n = len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                cnt +=1
        
        if cnt >= (n/2):
            return nums[i]
    
    return -1
    """
    # Hasmap Solution
    """    n = len(nums)
    mp = {}

    for num in nums:
        if num in mp:
            mp[num] +=1
        else:
            mp[num] = 1

    for num,count in mp.items():
        if count > n // 2:
            return num
    return -1
    """
# Moore Voting Algorithm
    n = len(nums)
    cnt = 0 
    el = 0
    for num in nums:
        if cnt == 0:
            cnt = 1
            el = num

        elif num == el:
            cnt +=1
        
        else:
            cnt -=1

    cnt1 = nums.count(el)

    if cnt1 > n//2:
        return el
    
    return -1


"""
        length=len(nums)//2
        nums.sort()
        return nums[length]
"""









if __name__ == "__main__":
    nums = [1,2,2,3,2,3,2,2]
    Solution = majorityelement(nums)
    print(nums)
    print(Solution)