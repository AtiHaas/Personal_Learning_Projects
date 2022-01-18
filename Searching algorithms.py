import random
import time

def analyze_func(func_name, *args):
    tic= time.time()
    func_name(*args)
    toc=time.time()
    seconds=toc-tic
    print(func_name , "Elapsed time --> ", seconds)

def generate_emails(n, list_of_names, list_of_domains):
    emails=[]
    for i in range(n):
        emails.append(list_of_names[random.randint(0, len(list_of_names)-1)] + list_of_domains[random.randint(0, len(list_of_domains)-1)])
    return emails



def bisection_recur(n,arr, start, stop):
    if start>stop:
        return "The number isnt in the list"
    else:
        middle=(start+stop)//2
        if n== arr[middle]:
            return middle
        elif n<arr[middle]:
            return bisection_recur(n, arr, start, middle-1)
        elif n >arr[middle]:
            return bisection_recur(n, arr, middle+1, stop)

def bisection_iter(n, arr):
    start=0
    stop=len(arr)-1
    while start<=stop:
        middle=(start+stop)//2
        if n == arr[middle]:
            return middle
        elif n< arr[middle]:
            stop= middle-1
        else:
            start=middle+1


def create_list(max_val):
    arr=[]
    for a in range(1, max_val+1):
        arr.append(a)
    return arr

    #____PROGRAM CODE____
list_of_domains=["@gmail.com", "@yahoo.com", ""]
list_of_names=["aela", "katika", "jozsi"]

emails=generate_emails(100, list_of_names, list_of_domains)

my_email="atihaas423@gmail.com"
emails.append(my_email)

sorted_emails= sorted(emails)

print(bisection_iter(my_email, sorted_emails))

print (analyze_func(bisection_iter, my_email, sorted_emails))
