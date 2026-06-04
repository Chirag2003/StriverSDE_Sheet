"""
Brute Force Approach
def movezeroes(arr,n):

    temp = [0]*n
    index = 0



    for num in arr:
        if num != 0:
            temp[index]= num
            index += 1

    for i in range(n):
        arr[i] = temp[i]

    return arr"""


def movezeroes(arr,n):

    i = 0 
    for j in range(n):
        if arr[j] != 0:
            arr[i],arr[j] = arr[j], arr[i]
            i+=1

    return arr
    



if __name__ == "__main__":
    arr1=[1,0,0,0,8]
    n = len(arr1)
    print(arr1)
    zeroes = movezeroes(arr1,n)
   
    print(zeroes)