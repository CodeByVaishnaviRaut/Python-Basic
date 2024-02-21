if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list1 = student_marks[query_name]
    n = len(list1)
    avg = sum(list1)/n
    print(f'{avg:.2f}')
