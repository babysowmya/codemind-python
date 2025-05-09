F1, P1, F2, P2 = map(int, input().split())
diff1 = abs(F1 - P1)
diff2 = abs(F2 - P2)
if diff1 < diff2:
    print("First")
elif diff2 < diff1:
    print("Second")
else:
    print("Both")
