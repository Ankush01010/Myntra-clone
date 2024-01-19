def f(arr,i):
    if(i == len(arr)):
        print(arr)
        return
    c1 = arr[i:]+arr[i].lower()+arr[i+1:]
    f(c1,i+1)
    c2 = arr[i:]+arr[i].upper()+arr[i+1:]
    f(c2,i+1)
arr="sjdd"
f(arr,0)