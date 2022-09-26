n = int(input()) 

if n%2 == 0:
    n = n-1

list_a = []
number = 1
while n!=0:
    list_a.append(number)
    number+=2
    n -= 1 
print(list_a)
