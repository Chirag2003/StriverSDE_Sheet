def removeElement(nums,val) -> int:
    n = len(nums)

    index = 0
    for j in range(n):
        if nums[j] != val:
            nums[index] = nums[j]
            index +=1
    return index


if __name__ == "__main__":
    arr1=[3,2,2,3,1,3,1,4,5]
    val = 3
    n = len(arr1)

    remove = removeElement(arr1,val)
    print(remove)
    print(arr1[:remove])

