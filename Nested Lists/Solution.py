if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
    students.sort(key=lambda x: x[1])
    second_lowest_score = sorted(set(score for name, score in students))[1]
    second_lowest_students = [name for name, score in students if score == second_lowest_score]
for i in sorted(second_lowest_students):
    print(i)
