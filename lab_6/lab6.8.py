a=[1,23,4,5]
b=5
for i in range(0,4):
    for j in range(i+1,4):
        if a[i]+a[j]==b:
            print i
            print j
