def LeftRotatebyOne(arr,n):
    temp = arr[0]

    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[-1] = temp
    return arr

if __name__ == "__main__":
    arr1=[1,2,5,7,8]
    n = len(arr1)
    print(arr1)
    rotate = LeftRotatebyOne(arr1,n)
    print(rotate)
