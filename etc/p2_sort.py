#성적이 낮은 순서로 학생 출력하기 

n = int(input())
student = []
for _ in range(n):
    tmp = input().split()
    student.append((tmp[0], int(tmp[1])))

student.sort(key = lambda student: student[1])
for x in student:
    print(x[0], end = " ")

