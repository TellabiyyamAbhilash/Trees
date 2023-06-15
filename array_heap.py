# code for tranforming the complete binary tree
# which is in array representation
# to a max heap


def heapify(arr,ind,n):
    largest = ind
    left = ind*2 + 1
    right = ind*2 + 2
    
    if left <=n and arr[largest]<arr[left]:
        largest = left
    if right <=n and arr[largest]<arr[right]:
        largest = right
        
    if ind != largest:
        temp = arr[ind]
        arr[ind] = arr[largest]
        arr[largest] = temp
        heapify(arr,largest,n)

def build_heap(arr,n):

    # in an array representaion of the complete binary tree
    # the inernal nodes index is below the " n//2 "
    # so looping it from that index to the 0th index
    for i in  range(n//2 -1 ,-1, -1):
        heapify(arr,i,n)

arr = [10,50,60,30,40,20,52]
n = len(arr)
build_heap(arr,n)

print(arr)