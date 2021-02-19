2.  Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.

lst = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    ele = int(input()) 
    if ele > 100 : 
        lst.append("over")
    else:
        lst.append(ele) 
print(lst)
