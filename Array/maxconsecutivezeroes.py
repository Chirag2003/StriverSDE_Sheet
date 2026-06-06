def findMaxConsecutiveOnes(nums):
        count = 0
        result = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            else:
                result = max(result,count)
                count = 0
        return max(result,count)


if __name__ == "__main__":
    arr1=[0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1]
    val = 3
    n = len(arr1)

    ones = findMaxConsecutiveOnes(arr1)
    print(ones)