# code for building a heap as we insert a node each time
# performed on the array representation.

def insert_node(arr,new_data):
    arr.append(new_data)
    n = len(arr)
    #prform only when the tree contains more the one node
    if n>1:
        # performing the heapification as the new node is inserted into the tree
        for i in  range(n//2 -1 ,-1, -1):
            heapify(arr,i,n)
    print(f"Max heap after inserting {new_data} :",arr)

def heapify(arr,ind,n):
    largest = ind
    left = ind*2 + 1 if (ind*2 + 1)<n else 0
    right = ind*2 + 2 if (ind*2 + 2)<n else 0
    
    # checking for the largest node in the parent and the children
    if left and left <=n and arr[largest]<arr[left]:
        largest = left
    if right and right <=n and arr[largest]<arr[right]:
        largest = right
    
    # swaping if the parent node is not the largest
    if ind != largest:
        temp = arr[ind]
        arr[ind] = arr[largest]
        arr[largest] = temp
        heapify(arr,largest,n)
        
arr = []
insert_node(arr,5)
insert_node(arr,8)
insert_node(arr,9)
insert_node(arr,6)
insert_node(arr,7)
insert_node(arr,10)



        
    
    
    