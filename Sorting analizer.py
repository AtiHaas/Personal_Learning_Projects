import time
import random

# ____ANALYZING ALGORITHMS______

def create_random_list(size, max_val):
    rand_list = []
    for i in range(size):
        rand_list.append(random.randint(1, max_val))
    return rand_list

def analyze_func(func_name, arr):
    tic= time.time()
    func_name(arr)
    toc=time.time()
    seconds=toc-tic
    print(func_name , "Elapsed time --> ", seconds)



# ______SORTING ALGORITHMS______

def merge_sorted(arr1, arr2):
    """
    This algorithym uses the deive and concure method. And it has a complexity of n*log(n)
    """

    sorted_arr=[]
    i , j= 0 , 0
    while i<len(arr1) and j<len(arr2):

        if arr1[i]<arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    if i<len(arr1):
        for k in range(i, len(arr1)):
            sorted_arr.append(arr1[k])
    elif j<len(arr2):
        for l in range (j, len(arr2)):
            sorted_arr.append(arr2[l])


    return sorted_arr

def devide_arr (arr):
    if len (arr)<2:
        return (arr[:])
    else:
        middle=len(arr)//2

        l1=devide_arr(arr[:middle])
        l2=devide_arr(arr[middle:])
        return merge_sorted(l1,l2)


def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot= arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num<pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            elif num>pivot:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)

def bubble_sort(arr):
    """
    This algorithm sorts the list of numbers by switching
    the neighbours many times
    """
    comparisons=0
    for i in range(0, (len(arr)-1)):
        comparisons +=1
        for a in range(0,(len(arr)-1)):
            comparisons +=1
            if arr[a]>arr[a+1]:
                b=arr[a]
                arr[a]=arr[a+1]
                arr[a+1]=b
    return arr  , comparisons

def selction_sort(arr):
    """
    This algorithm sorts the list of numbers by starting at the lowest index and
    switching the number until it becomes the lowest
    """
    comparisons=0
    for i in range(0, (len(arr)-1)):
        comparisons +=1
        for a in range(i+1, len(arr)):
            comparisons +=1
            if arr[i]>arr[a]:
                b=arr[i]
                arr[i]=arr[a]
                arr[a]=b
    return arr, comparisons

def insertion_sort(arr):
    """
    This algorithm sorts the list of numbers by
    """

    for key in range(1, len(arr)):
        if arr[key]<arr[key-1]:
            b=arr[key]
            arr[key]=arr[key-1]
            arr[key-1]=b

            for key2 in range(1, key), -1:
                if arr[key2]<arr[key2-1]:
                    c=arr[key2]
                    arr[key2]=arr[key2-1]
                    arr[key2-1]=c

    return arr



    # _____PROGRAM EXECUTION_____

size=10000000
length=10000
run_times=3


for i in range(run_times):
    print("Run number: ", i+1)
    l = create_random_list(size, length)
    l2=l
    #analyze_func(bubble_sort, l2)
    analyze_func(quicksort, l)
    analyze_func(sorted, l)
    #analyze_func(devide_arr, l)
    print("_"*40)
