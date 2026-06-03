def SecondLargestElement(arr,n):
    if n < 2: 
        return -1
    
    largest = float("-inf")
    slargest = float("-inf")

# First change second largest and then assign largest
    for i in range(n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        
        elif arr[i] != largest and arr[i] > slargest:
            slargest = arr[i]

    return slargest


def SecondSmallestElement(arr,n):
    if n < 2: 
        return -1
    
    small = float("inf")
    ssmall = float("inf")

# First change second largest and then assign largest
    for i in range(n):
        if arr[i] < small:
            ssmall = small
            small = arr[i]
        
        elif arr[i] != small and arr[i] < ssmall:
            ssmall = arr[i]

    return ssmall

if __name__ == "__main__":
    arr1=[1,2,5,7,8]
    n = len(arr1)

    second = SecondLargestElement(arr1,n)
    ssmall = SecondSmallestElement(arr1,n)
    print(second)
    print(ssmall)