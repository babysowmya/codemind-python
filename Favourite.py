x = int(input())
for i in range(1,x+1):
    a = int(input())
    if a%2==0 and a%7==0:
        print("Alice")
    elif a%2!=0 and a%9==0:
        print("Bob")
    else:
        print("Charlie")
