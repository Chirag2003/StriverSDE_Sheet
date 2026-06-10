def twoSum(arr ,target) -> List[int]:
# Brute Force Solution O(N2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j : continue
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
# Best solution acc to LC
        mp = {}
        for i, num in enumerate(nums):
            if target - num in mp:
                return[i,mp[target-num]]
            mp[num] = i
        # Optimal Solution but requires array sorted
        # sum = 0 
        # left = 0
        # right = len(nums)-1

        # nums.sort()
        # print(nums)

        # while left < right:
        #     sum = nums[left] + nums[right]
            
        #     if sum == target:
        #         return [left,right]
        #     elif sum < target:
        #         left+=1
        #     else: 
        #         sum > target
        #         right-=1

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 7
    sum = twoSum(nums,target)
    print(sum)
            
           
        