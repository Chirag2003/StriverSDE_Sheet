# Optimal Solution

def LargestElement(arr,n):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
        
    return max


if __name__ == "__main__":
    arr1 = [2,1,5,6,7]
    n = len(arr1)

    max = LargestElement(arr1,n)
    print(max)