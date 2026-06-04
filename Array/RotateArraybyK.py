
""""
Brute Force Approach
def LeftRotatebyK(arr,n,k):
    if n==0:
        return arr
    
    k = k%n

    for i in range(k):
        temp = arr[:k]

    for i in range(k,n):
        arr[i-k]= arr[i]

    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]

    return arr
"""  

def reverse(arr,s,e):
    while s<e:
        arr[s],arr[e]= arr[e],arr[s]
        s+=1
        e-=1

    
def LeftRotatebyK(arr,n,k):

    k = k%n

    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

    return arr

def RightRotatebyK(arr,n,k):
    k=k%n

    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)

    return arr

if __name__ == "__main__":
    arr1=[1,2,5,7,8]
    n = len(arr1)
    k=2
    print(arr1)
    rotate = LeftRotatebyK(arr1.copy(),n,k)
    right_rotate = RightRotatebyK(arr1.copy(),n,k)
    print(rotate)
    print(right_rotate)