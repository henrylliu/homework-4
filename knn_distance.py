import random 

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    """Finds the kth smallest element in arr, with k=1 being the closest neighbor based on distance"""
    if low <= high:
        pi = partition(arr, low, high)
        rank = pi - low + 1  # Makes it 1-indexed
        if rank == k:
            return arr[pi]
        elif rank > k:
            return quickselect(arr, low, pi - 1, k)
        else:
            return quickselect(arr, pi + 1, high, k - rank)
    return None

def knn_distance(arr, q, k):
    """ Returns the kth closest neighbor to the query point q

    Args: 
        - arr (List): A 1-D list representing different points
        - q (int): The query point
        - k (int): The kth closest neighbor in arr to q, with k=1 being the closest neighbor to q

    Returns:
        - tuple(distance, point): Returns the distance between the kth closest point and the respective point

    The overall runtime complexity should be O(n), where n is the size of the input array
    """

    n = len(arr)
    diff_arr = [(abs(x - q), x) for x in arr]
    
    return quickselect(diff_arr, 0, n - 1, k)



print(knn_distance([3, 10, 52, 15], 19, 3))