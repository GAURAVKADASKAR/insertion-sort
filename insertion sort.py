''' insertion sort'''
a=[5,4,3,2,1]
for i in range(len(a)):
    tem=a[i]
    j=i-1
    while((a[j]>tem) and (j>=0)):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=tem
for i in range (len(a)):
    print(a[i])