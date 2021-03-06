string1 = input("Type a string : ")
char =string1[0]
string1 = string1.replace(char,'$')
print(char+string1[1:])