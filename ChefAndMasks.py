x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    if a*100>=b*10:
        print("Cloth")
    else:
        print("Disposable")
