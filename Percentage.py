if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    z = student_marks[query_name]
    res = sum(z)/len(z)
    print(f"{res:.2f}")
