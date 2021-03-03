max=int(input("please enter the maximum value: "))

even_Sum=0

odd_Sum=0
num=1
while (num<=max):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
    num+=1
print("The sum of Even numbers 1 to entered number",even_Sum)
print("The sum of odd numbers 1 to entered number",odd_Sum)
 