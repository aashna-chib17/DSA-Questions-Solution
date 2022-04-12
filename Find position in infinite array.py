# Find position of an element in a sorted array of infinite numbers

def findPos(key,arr):
    left = 0
    right = 1 
    val = arr[0]
    while val<key:
        left = right
        right = 2*right
        val = arr[right]
    return bin_search(left,right,arr,key)
    
def bin_search(low,high,arr,key):
    if low <= high:
        mid = low + (high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]>key:
            return bin_search(low,mid-1,arr,key)
        else:
            return bin_search(mid+1,high,arr,key)
    return -1 
arr = list(map(int,input().split())) 
pos = int(input())
ans = findPos(pos,arr)
if ans == -1:
    print('Key not present')
else:
    print('Key present at :',ans)
            
