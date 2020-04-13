a=[34,67,3,76,4,6,36,7,8,9]

def insertion(ar):

    for i in range(1,len(ar)):

        key=ar[i]
        j=i-1

        while key<ar[j] and j>=0:
            ar[j+1]=ar[j]
            j-=1
            print(ar[j+1])
        ar[j+1]=key
    return ar

print(insertion(a))