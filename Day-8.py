# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = dict()
for i in range(n):
    s = input()
    s = s.split()
    phonebook[s[0]] = phonebook.get(s[0],s[1])

while True:
    try:
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break
