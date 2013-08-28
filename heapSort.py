def heapSort(A):
    heapify(A)
    length = len(A)
    end = length -1
    while end > 0:
        A[0], A[end] = A[end], A[0]
        end = end -1 
        siftDown(A, 0, end)        
    return A

def heapify(A):
    heapsize = len(A)
    parent = (heapsize -2)/2
    while parent >= 0:
        siftDown(A, parent, heapsize -1)
        parent = parent -1

def siftDown(A, start, end):
    root = start
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root
    if left <= end and A[left] > A[largest]:
        largest = left
    if right <= end and A[right] > A[largest]:
        largest = right
    if largest != root:
        A[root], A[largest] = A[largest], A[root]
        siftDown(A, largest, end)

        

