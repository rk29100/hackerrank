# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0,n):
    string=input()
    print(string[::2],string[1::2])
