s=input("Enter String: ")
n=int(input("Enter no: "))
for  i in range(1,n+1):
    for char in s:
        print(char*i,end="")
    print()
