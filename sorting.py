from datetime import datetime
import time
import numpy.random
from numpy.random import randint
import sys

sys.setrecursionlimit(10**9)
# To take input from command line
sorttype = str(sys.argv[1])
size = int(sys.argv[2])
typ = str(sys.argv[3])

if typ in ['s']:
    arr = numpy.arange(1,size)      #sequence of arr 1 to n
    arr = numpy.int64(arr)
    print("Generated input:",arr)
elif typ in ['c']:
    arr = numpy.zeros((size,), dtype=int)   #array of all zeroes
    print("Generated input:",arr)
elif typ in ['r']:
    arr = randint(0,size,size)          #array of random integers
    arr = numpy.int64(arr)
    print("Generated input:",arr)
else:
    sys.exit("Invalid type of data.")

#current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        # Find minimum element from unsorted part
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[min_index] > arr[j]: 
                min_index = j 
        # Swap the found minimum element with the first element         
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

def quick_sort(arr):
    def swap(arr,a,b):
        arr[a],arr[b] = arr[b],arr[a]
    def partition(arr,start,end):
        median = (end - 1 - start) // 2
        median = median + start
        left = start + 1
        if (arr[median] - arr[end-1])*(arr[start]-arr[median]) >= 0:
            swap(arr,start,median)
        elif (arr[end - 1] - arr[median]) * (arr[start] - arr[end - 1]) >=0:
            swap(arr,start,end - 1)
        pivot = arr[start]
        for right in range(start,end):
            if pivot > arr[right]:
                swap(arr,left,right)
                left = left + 1
        swap(arr,start,left-1)
        return left-1
    def quickSortHelper(arr,start,end):
        if start < end:
            splitPoint = partition(arr,start,end)
            quickSortHelper(arr,start,splitPoint)
            quickSortHelper(arr,splitPoint+1,end)
    quickSortHelper(arr,0,len(arr))

start = time.time()

if sorttype in ['i']:
    insertion_sort(arr)
elif sorttype in ['s']:
    selection_sort(arr)
elif sorttype in ['q']:
    quick_sort(arr)
else:
    sys.exit("Invalid sorting technique")

print ("Sorted array is:", arr)

print("Time taken to sort:",time.time()-start,"seconds.")

if (all(arr[i] <= arr[i + 1] for i in range(len(arr)-1))):
    print("Data correctly sorted after running algorithm.")
else:
    print("Data incorrectly sorted after running algorithm.")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)