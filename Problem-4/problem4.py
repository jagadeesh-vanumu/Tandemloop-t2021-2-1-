a = [int(x) for x in input().split(",")] 

dict_a = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}


for i in a:
    for j in range(1,10):
        if i%j == 0:
            dict_a[j]+=1 

print(dict_a)
