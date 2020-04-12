a=[34,67,3,76,4,6,36,7,8,9]

def insertion(ar):
    for i in range(1,len(ar)):
        print('-----------------------------------------')
        key = ar[i]
        j=i-1
        print('key:',key,"j:",j)
        while j>=0 and key<ar[j]:
            print("ar[j]:",ar[j])
            print('ar[j+1]:',ar[j+1])
            ar[j+1]=ar[j]
            
            j-=1
        ar[j+1]=key
        print(ar)
    return ar
print(insertion(a))