# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    last = len(arr)
    for i in range(last):
        smallest_index = i
        
        for j in range(i+1, last):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # swap
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap = True
    while swap is True:
        swap = False
        for idx, el in enumerate(arr):
            try:
                if el > arr[idx + 1]:
                    arr[idx], arr[idx + 1] = arr[idx + 1], el
                    swap = True
            except IndexError:
                pass
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=256):
    # initializing counr array with zeros
    count = [0] * (maximum + 1)

    # counting elements in arr and putting counts in count
    for el in arr:
        if el < 0:
            return "Error, negative numbers not allowed in Count Sort"
        count[el] += 1

    i = 0
    for el in range(maximum + 1):
        for c in range(count[el]):
            arr[i] = el
            i += 1
        
    return arr
