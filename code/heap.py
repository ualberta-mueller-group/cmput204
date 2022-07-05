'''
Binary min-heap implementation.
The heap is a binary tree that is implicitly stored in a list.
Node n has parent at index floor(n-1/2), and children at indices 
2*n + 1 and 2*n + 2.
We will use this heap datastructure as a priority queue.

Written by Jesse Huard, with small fixes to the documentation 
by Martin Mueller.
'''

def parent(index):
    return (index - 1) // 2


def makeQueue(distance):
    '''
    Create a new heap-based priority queue from the given distance dict.
    '''
    heap = []
    for node in distance:
        insert(heap, (distance[node], node))
    return heap


def insert(heap, element):
    '''
    Insert a new element with the given value into the heap.
    Takes O(lg n) time.
    '''
    value = element[0]
    heap.append(element)
    index = len(heap) - 1

    while value < heap[parent(index)][0] and index > 0:
        heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
        index = parent(index)


def decreasekey(heap, key, value):
    '''
    Decrease the value of the element with the given key.
    This takes O(n) time since we do a linear search for the key.
    '''
    for index, element in enumerate(heap):
        if (element[1] == key):
            assert element[0] > value
            heap[index] = (value, element[1])

            while value < heap[parent(index)][0] and index > 0:
                heap[index], heap[parent(index)] = heap[parent(index)], heap[index]
                index = parent(index)

            break


def deletemin(heap):
    '''
    Delete the minimal element from the heap.
    This takes O(lg n) time.
    '''
    min_element = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    index = 0

    while True:
        smallest = index
        if 2 * index + 1 < len(heap) and heap[index] > heap[2 * index + 1]:
            smallest = 2 * index + 1

        if 2 * index + 2 < len(heap) and heap[index] > heap[2 * index + 2]:
            smallest = 2 * index + 2

        if smallest == index:
            break

        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest

    return min_element
