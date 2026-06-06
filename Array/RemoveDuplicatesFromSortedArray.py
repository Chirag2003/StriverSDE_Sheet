def RemoveDuplicates(nums,n,):
    n = len(nums)

    index = 0
    for j in range(n):
        if j==0 or nums[j] != nums[j-1]:
            nums[index] = nums[j]
            index+=1
    
    return index


if __name__ == "__main__":
    arr1=[1,2,5,5]
    n = len(arr1)

    duplicates = RemoveDuplicates(arr1,n)
    print(duplicates)
    print(arr1[:duplicates])

